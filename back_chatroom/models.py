from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(
        upload_to='chatroom_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.topic

