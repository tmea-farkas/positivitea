from django.db import models
from django.contrib.auth.models import User
from back_posts.models import Post
from back_comments.models import Comment

class Like(models.Model):
    """
    Like model for users to be able to like posts & comments.
    Preventing users to like their own or to double like.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'post', 'comment')
        #to ensure the user can only like a post or comment once
        constraints = [
            models.CheckConstraint(check=(
                models.Q(post__isnull=False, comment__isnull=True) |
                models.Q(post__isnull=True, comment__isnull=False)
            ),
            name= 'like_either_post_or_comment',
            )
        ]
        
        
    
    def __str__(self):
        if self.post:
            return f"{self.owner.username} liked post {self.post.id}"
        if self.comment:
            return f"{self.owner.username} liked comment {self.comment.id}"







