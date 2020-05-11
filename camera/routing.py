from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'camera/ws/(?P<kind>host|client)/(?P<room_name>\w+)/$',
            consumers.VideoConsumer),
]
