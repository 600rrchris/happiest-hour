from django.shortcuts import render
# Create your views here.

def users(request):
    return render(request, 'users.html')
def groups(request):
    return render(request, 'groups.html')
