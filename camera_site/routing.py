from channels.routing import ProtocolTypeRouter, URLRouter
import camera.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
        camera.routing.websocket_urlpatterns
    ),
})
