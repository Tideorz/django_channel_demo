from django.shortcuts import render

# Create your views here.

from django.db import transaction
from django.shortcuts import redirect, render
from model import Room, Message

import haikunator



def new_room(request):
    """create a new room and redict to it"""
    new_room = None

    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()  
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(chat_room, label=label)


def chat_room(request, label):
    """show the lastest messages""" 

    room_object = Room.objects.filter(label=label)[0]
    messages_list = reversed(room.messages.order_by('-timestamp')[50])

    context = {
        'room': room,
        'messages': messages_list
    }
