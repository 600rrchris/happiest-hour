from django.shortcuts import render
from .models import User, Group, Event, Comment
# Create your views here.
def home(request):
    return HttpResponse('<h1>Happiest Hour</h1>')
def users(request):
    return render(request, 'users.html')

def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups' : groups})

def home(request):
  return render(request, 'home.html')

