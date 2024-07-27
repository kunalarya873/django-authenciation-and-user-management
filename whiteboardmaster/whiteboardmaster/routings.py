from django.urls import path
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from whiteboard.consumers import BoardConsumer
from django.core.asgi import get_asgi_application

websocket_patterns = [
    path('ws/board/', BoardConsumer.as_asgi()),  # Specify the WebSocket path
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':
        URLRouter(websocket_patterns)
})
