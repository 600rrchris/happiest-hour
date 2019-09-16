from django.shortcuts import render, redirect
from .models import User, Group, Event, Comment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def events_index(request):
    return render(request, 'events/index.html')

def events_new(request):
    return render(request, 'events/new.html')

def events_details(request):
    return render(request, 'events/details.html')

def groups_index(request):
    return render(request, 'groups/index.html')

def groups_new(request):
    return render(request, 'groups/new.html')

def groups_details(request):
    return render(request, 'groups/details.html')         

def users(request):
    return render(request, 'users.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

