# chat/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^async/(?P<room_name>[^/]+)/$', views.async_room, name='async_room'),
]