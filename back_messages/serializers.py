from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers, generics
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'Message content cannot be empty'
            )
        if len(value) < 2:
            raise serializers.ValidationError(
                'Message is too short.'
            )
        return value

    def validate_image(self, value):
        if value is None:
            return value
    
        if value.size > 1024 * 1024 *2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        
        valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
        ext = value.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise serializers.ValidationError(
                'Unsupported file format.'
                'Only JPG, JPEG, PNG, and GIF are allowed.'
            )

        return value

    class Meta:
        model = Message
        fields = [
            'id', 'chatroom', 'owner', 'is_owner',
            'content', 'image', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class MessageDetailSerializer(MessageSerializer):
    chatroom = serializers.ReadOnlyField(source='chatroom.id')
    owner = serializers.ReadOnlyField(source='owner.username')
