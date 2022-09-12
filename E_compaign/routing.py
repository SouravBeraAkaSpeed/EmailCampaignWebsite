from django.urls import re_path
from . import consumer

websocket_urlpattern=[
    re_path(r'ws/notification/$',consumer.NotificationConsumer.as_asgi()),
]