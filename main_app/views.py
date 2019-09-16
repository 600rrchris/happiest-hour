from django.shortcuts import render, redirect
from .models import User, Group, Event, Comment, Poll
from .forms import PollForm
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

def events_poll(request):
    return render(request, 'events/poll.html')

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
    fields = ['title',[Group], 'time', 'date', 'location', 'Comment']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'        


def index(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            chosen_locations_options = form.cleaned_data.get('chosen_locations_options', [])
            other_location_name = form.cleaned_data.get('other_location_name', '')
            Poll.bulk_poll(chosen_locations_options + [other_location_name])
        message = 'Thank You For Your Contribution!'
    elif request.method == 'GET':
        message = ''

    form = PollForm()
    return render(request, 'templates/events/survey.html', {'form': form, 'message': message})