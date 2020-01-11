from django.contrib import messages
from django.shortcuts import render, redirect
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
