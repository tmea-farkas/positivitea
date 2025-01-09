from django.db import models
from django.contrib.auth.models import User
from back_profiles.models import Profile

class Follower(models.Model):
    owner = models.ForeignKey(
        User, related_name='follower', on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'followed')
        
        
    
    def __str__(self):
        return f'{self.owner} {self.followed}'