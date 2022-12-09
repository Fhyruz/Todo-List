from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    todo_list= Todo.objects.order_by('id')
    todo_form= TodoForm()
    context= {'todo_list':todo_list, 'todo_form': todo_form}
    return render(request, 'todo/index.html', context)

def addTodo(request):
    todo_form = TodoForm(request.POST)

    if todo_form.is_valid():
        new_todo= Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def complete(request, list_id):
    todo= Todo.objects.get(pk=list_id)

    todo.complete= True
    todo.save()

    return redirect('index')

def deletecompleted(request):
    Todo.objects.filter(complete__exact= True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
