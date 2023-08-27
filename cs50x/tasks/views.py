from django.shortcuts import render

# Create your views here.
tasks = ['Do my homeworks', 'practice Python', 'check my emails']

def index(request):
    return render(request, 'tasks/index.html',{
        "mytasks": tasks
    })

def add(request):
    return render(request, 'tasks/add.html')