from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from trips.consumers import UberConsumer

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter([
        path('taxi/', UberConsumer.as_asgi()),
    ]),
})