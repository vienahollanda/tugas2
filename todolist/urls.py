
from django.urls import path
from todolist.views import register, login_user, logout_user, show_tasks, tambah_task, task_deleted, task_completed, show_task_json, add_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_tasks, name='show_tasks'),
    path('create-task/', tambah_task, name='tambah_task'),
    path('delete/<int:id>', task_deleted, name='task_deleted'),
    path('toggle/<int:id>', task_completed, name='task_completed'),
    path('json/', show_task_json, name='show_task_json'),
    path('add/', add_task_ajax, name='add_task_ajax'),
]