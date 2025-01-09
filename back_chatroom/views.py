from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Chatroom
from .serializers import ChatroomSerializer
from backend_api.permissions import IsOwnerOrReadOnly


class ChatroomList(APIView):
    serializer_class = ChatroomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        chatrooms = Chatroom.objects.all()
        serializer = ChatroomSerializer(
            chatrooms, many=True, context={'request':request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatroomSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class ChatroomDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChatroomSerializer

    def get_object(self, pk):
        try:
            chatroom = Chatroom.objects.get(pk=pk)
            self.check_object_permissions(self.request, chatroom)
            return chatroom
        except Chatroom.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        chatroom = self.get_object(pk)
        serializer = ChatroomSerializer(
            chatroom, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        chatroom = self.get_object(pk)
        serializer = ChatroomSerializer(
            chatroom, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        chatroom = self.get_object(pk)
        chatroom.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
