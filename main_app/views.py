from django.shortcuts import render, redirect
from .models import Group, Event, Comment, Account
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from main_app.forms import SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()

def users(request):
    return render(request, 'users.html')
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

@login_required
def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html',{'events' : events})

@login_required
def events_new(request):
    return render(request, 'events/new.html')

@login_required
def events_details(request):
    return render(request, 'events/details.html')

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'
    success_url = '/events/index'
    
class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__' 
    success_url = '/events/index'

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/index'

  
@login_required
def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'groups' : groups})

@login_required
def groups_new(request):
    return render(request, 'groups/new.html')

@login_required
def groups_details(request):
    return render(request, 'groups/details.html')         

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'users']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        success_url = '/groups/index/' 
    
class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = '__all__'
    success_url = '/groups/index'
    
class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/groups/index'