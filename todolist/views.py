from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.form import TaskForms
import datetime
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_tasks(request):
    user_logged_in = request.user
    data_tasks = Task.objects.filter(user=user_logged_in)
    context = {
        'list_tasks': data_tasks,
        'username': user_logged_in.get_username(),
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def tambah_task(request):
    if request.method == "POST":
        form = TaskForms(request.POST)
        date = datetime.date.today()
        if form.is_valid():
            form = TaskForms(request.POST)
            task = form.save(commit=False)
            task.user = request.user
            task.date = date
            form.save()
            return HttpResponseRedirect(reverse('todolist:show_tasks'))
    else:
        form = TaskForms()
    return render(request, 'create-task.html', {'form': form})


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_tasks"))  # membuat response
            response.set_cookie('last_login',
                                str(datetime.datetime.now()))  # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
