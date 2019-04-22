# chat/view.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def async_room(request, room_name):
    return render(request, 'chat/async_room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })