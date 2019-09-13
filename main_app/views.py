from django.shortcuts import render
from .models import User, Group, Event, Comment
# Create your views here.

def users(request):
    return render(request, 'users.html')

def groups(request):
    return render(request, 'groups.html')

def home(request):
  return render(request, 'home.html')

hello