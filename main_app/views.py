from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
<<<<<<< HEAD
    return HttpResponse('<h1>Happiest hour</h1>')
def users(request):
    return render(request, 'users.html')
def groups(request):
    return render(request, 'groups.html')
=======
    return HttpResponse('<h1>Happiest hour:-)</h1>')
>>>>>>> eed9a1ebe26e84c9d9612f417c1e284893756b2f
