from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def saeed(request):
    return HttpResponse('hello, saeed')

def javad(request):
    return HttpResponse('hello, javad')

def greet(request, name):
    return render(request, 'hello/greet.html', {
        "name": name.capitalize()
    })

