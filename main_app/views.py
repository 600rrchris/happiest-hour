from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Happiest hour</h1>')
def users(request):
    return render(request, 'users.html')
def groups(request):
    return render(request, 'groups.html')
