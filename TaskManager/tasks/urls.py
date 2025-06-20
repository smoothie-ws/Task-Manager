from django.contrib import admin
from django.urls import path
from . import views


app_name = 'app_tasks'

urlpatterns = [
    path('tasks-list/', views.tasks_list, name='tasks_list'),
    path('task/<slug:task_slug>', views.task_view, name='task_view'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-delete/<slug:task_slug>', views.task_delete, name='task_delete'),
]
