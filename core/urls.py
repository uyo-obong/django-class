from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('todo/<int:pk>/edit', views.edit_todo, name='todo.edit'),
    path('todo/<int:pk>/delete', views.delete_todo, name='todo.delete')
]
