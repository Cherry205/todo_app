from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def todo_list_html(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        completed = request.POST.get("completed") == "on"
        Todo.objects.create(title=title, description = description , completed = completed)
        
        return redirect('todo-html')
    
    todos = Todo.objects.all()
    return render(request, 'todo/list.html',{'todos' : todos})


def todo_update_html(request, pk ):
    todo = get_object_or_404(Todo, pk = pk)
    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.completed = request.POST.get("completed") == "on"

        todo.save()
        return redirect('todo-html')
    
    return render(request,'todo/update.html',{'todo':todo})

def todo_delete_html(request,pk):
    todo = get_object_or_404(Todo, pk = pk)
    todo.delete()
    return redirect('todo-html')
    
