from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path(r"ws/ai-demo/", consumers.ChatConsumerDemo.as_asgi(), name="ws_ai_demo_new_chat"),
 ]