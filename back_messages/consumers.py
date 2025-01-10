import json
import base64
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from back_chatroom.models import Chatroom
from .serializers import MessageSerializer

class MessageConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        self.chatroom_group_name = f'chatroom_{self.chatroom_id}'

        await self.channel_layer.group_add(
            self.chatroom_group_name,
            self.channel_name
        )

        chatroom = Chatroom.objects.get(id=self.chatroom_id)
        past_messages = Message.objects.filter(
        chatroom=chatroom).order_by('created_at')

        for message in past_messages:
            await self.send(text_data=json.dumps({
                'username': message.owner.username,
                'message': message.content,
                'timestamp': message.created_at.isoformat(),
                'image_url': message.image.url if message.image else None,
            }))

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chatroom_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        image = text_data_json['image']
        user = self.scope['user']

        if image:
            format, imgstr = image.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(imgstr),
            name=f'{user.username}_image.{ext}')

            image_file = File(image_file)
        else:
            image = None
        

        message = Message.objects.create(
            owner=user,
            chatroom=chatroom,
            content=content,
            image=image if image else None
        )

        message_serializer = MessageSerializer(message)

        await self.channel_layer.group_send(
            self.chatroom_group_name,
            {
                'type': 'chatroom_message',
                'message': message_serializer.data
            }
        )
    
    async def chatroom_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message['content'],
            'username': message['owner'],
            'timestamp': message['created_at'],
            'image_url': message.get('image_url', None),
        }))
