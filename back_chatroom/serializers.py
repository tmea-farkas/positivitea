from rest_framework import serializers
from .models import Chatroom

class ChatroomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    

    def validate_image(self, value):
        if value is None:
            return value
    
        if value.size > 1024 * 1024 *2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Chatroom
        fields = [
            'id', 'topic', 'description', 'image', 
            'created_at', 'updated_at', 'owner', 'is_owner'
        ]