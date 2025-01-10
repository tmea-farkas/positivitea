from rest_framework import generics, permissions
from backend_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    # List or create post if logged in
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # Fetch, edit or create a post if user == owner
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()