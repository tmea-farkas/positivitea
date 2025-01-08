from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class CanLikeContent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, like):
            if obj.post and obj.post.owner == request.user:
                return False
            if obj.comment and obj.comment.owner == request.user:
                return False
        return True
