import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import re_path
from home.consumers import GameRoom

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tictac.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r'^play/(?P<room_code>\w+)/$', GameRoom.as_asgi()),
            ]
        )
    ),
})
