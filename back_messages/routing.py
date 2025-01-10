from django.urls import re_path
from .consumers import MessageConsumer

websocket_urlpatterns = [
    re_path(r'ws/chatroom/(P<chatroom_id>\d+)/$', MessageConsumer.as_asgi()),
]