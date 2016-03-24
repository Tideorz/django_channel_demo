"""url list handled by chat app"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^new/$', view.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})', view.chat_room, name='chat_room'),
]
