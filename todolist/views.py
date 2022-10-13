from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from todolist.form import TaskForms
import datetime
from django.core import serializers
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_tasks(request):
    user_logged_in = request.user
    data_tasks = Task.objects.filter(user=user_logged_in)
    form = TaskForms()
    context = {
        'list_tasks': data_tasks,
        'username': user_logged_in.get_username(),
        'last_login': request.COOKIES['last_login'],
        'form': form,
    }
    return render(request, "todolist.html", context)

def show_task_json(request):
    data_tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_tasks), content_type="application/json")

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


@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    # mengecek apakah user sudah log in
    if request.user.is_authenticated:
        # Ambil form-nya dari http request
        form = TaskForms(request.POST)
        response_data = {}

        # Handle jika form valid dan method request adl. POST
        if request.method == 'POST' and form.is_valid():
            # Ambil title & description dari form, buat task baru, lalu redirect
            # ke halaman utama
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_task = Task.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            response_data['title'] = title
            response_data['description'] = description
            response_data['date'] = datetime.date.today()
            return JsonResponse(response_data);

        # melakukan render pada halaman add task
        context = {
            'form': form,
        }
        return render(request, 'create-task.html', context)
    else:
        return redirect('todolist:login')

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

@login_required(login_url='/todolist/login/')
def task_deleted(request, id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('todolist:show_todolist')
    else:
        return redirect('todolist:login_user')


@login_required(login_url='/todolist/login/')
def task_completed(request, id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=id)
        task.is_finished = not task.is_finished
        task.save()
        return redirect('todolist:show_todolist')
    else:
        return redirect('todolist:login_user')
