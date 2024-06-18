from  django.urls import path 
from .consumers import *
from django.urls import re_path


websocket_urlpatterns = [
    re_path("ws/chatroom/(<room_name>", ChatroomConsumer.as_asgi()),
]