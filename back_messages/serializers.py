from rest_framework import serializers, generics
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

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

    class Meta:
        model = Message
        fields = [
            'id', 'chatroom', 'owner', 'is_owner',
            'content', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class MessageDetailSerializer(MessageSerializer):
    chatroom = serializers.ReadOnlyField(source='chatroom.id')
    owner = serializers.ReadOnlyField(source='owner.username')
