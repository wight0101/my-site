from django.shortcuts import render, redirect
from .models import *
from .forms import RoomForm, NewUserForm
from django.db.models import Q
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' 

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        
        ) 
    
    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request, pk):
    try:
        room = Room.objects.get(pk=pk)  
    except Room.DoesNotExist:
        room = None
    context = {"room": room}
    return render(request, 'base/room.html', context)



def CreateRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form': form}
    return render(request, 'base/create-room.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/update_room.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete-room.html', {'obj': room})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Збережіть створеного користувача у змінну user
            login(request, user)  # Увійдіть користувача після реєстрації
            return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()  # Ініціалізуйте форму для методу GET

    return render(request, 'base/register.html', {'form': form})

def login(request):
    context = {}
    return render(request, 'base/login_register.html', context)