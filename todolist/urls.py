
from django.urls import path
from todolist.views import register, login_user, logout_user, show_tasks, tambah_task

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_tasks, name='show_tasks'),
    path('create-task/', tambah_task, name='tambah_task'),
]