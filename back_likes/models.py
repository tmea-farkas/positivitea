from django.db import models
from django.contrib.auth.models import User
from back_posts.models import Post

class Like(models.Model):
    """
    Like model for users to be able to like posts & comments.
    Preventing users to like their own or to double like.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']
        #to ensure the user can only like a post once
        
        
    
    def __str__(self):
        return f'{self.owner} {self.post}'







