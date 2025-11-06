from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Message

def home(request):
    return render(request, "home.html")

def room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    return render(request, "room.html", {
        "username": username,
        "room": room,
        "room_details": room_details,
    })

def checkview(request):
    room = request.POST["room_name"]
    username = request.POST["username"]

    room_obj, created = Room.objects.get_or_create(name=room)
    return redirect(f"/{room}/?username={username}")

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    room = Room.objects.get(id=room_id)
    new_message = Message.objects.create(
        value=message,
        user=username,
        room=room
    )
    new_message.save()
    return HttpResponse("Message sent successfully!")
