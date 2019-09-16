from django.shortcuts import render, redirect
from .models import User, Group, Event, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required
def events_index(request):
    return render(request, 'events/index.html')

@login_required
def events_new(request):
    return render(request, 'events/new.html')

@login_required
def events_details(request):
    return render(request, 'events/details.html')

@login_required
def groups_index(request):
    return render(request, 'groups/index.html')

@login_required
def groups_new(request):
    return render(request, 'groups/new.html')

@login_required
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

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['users', 'name']
    success_url = '/groups/'  

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/groups/'

class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = '__all__'

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'location', 'time', 'date']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'        


