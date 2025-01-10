from rest_framework import generics, permissions
from backend_api.permissions import IsOwnerOrReadOnly
from .models import Message
from .serializers import MessageSerializer, MessageDetailSerializer

class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]