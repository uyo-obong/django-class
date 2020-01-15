from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import TodoForm
from .models import Todo


def index(request):

    todo = Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published_at = timezone.now()
            blog.save()
            messages.success(request, 'Todo created successfully.')
            return redirect('/')
    else:
        form = TodoForm()

    return render(request, 'index.html', {'form': form, 'todos': todo})


def edit_todo(request, pk):
    todos = Todo.objects.all()
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'todo updated successfully')
            return redirect('/')
    else:
        form = TodoForm(instance=todo)
        return render(request, 'index.html', {'form': form, 'todos': todos})


def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('/')