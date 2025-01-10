from django.db import models
from django.contrib.auth.models import User
from back_chatroom.models import Chatroom

class Message(models.Model):
    '''
    Model for real time messaging within chatrooms, so users can
    instantly see responses rather than having to reload the page
    '''
    chatroom = models.ForeignKey(
        Chatroom, on_delete=models.CASCADE, related_name='messages')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    attachment = models.FileField(
        upload_to='chatroom_attachments/', blank=True, null=True
    )

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        if self.is_deleted:
            return f"Deleted message in {self.chatroom.title}"
        return f"Message from {self.owner.username} in {self.chatroom.title}"