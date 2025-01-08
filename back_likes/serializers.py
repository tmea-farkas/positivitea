from rest_framework import serializers
from .models import Like
from back_comments.models import Comment
from back_posts.models import Post

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()

    post_title = serializers.ReadOnlyField(source='post.title', required=False)
    post_id = serializers.ReadOnlyField(source='post.it', required=False)

    comment_content = serializers.ReadOnlyField(
        source='comment.content', required=False)
    comment_id = serializers.ReadOnlyField(
        source='comment.id', required=False)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'is_owner',
            'post_id', 'post_title', 'comment_id', 'comment_content',
            'created_at'
        ]