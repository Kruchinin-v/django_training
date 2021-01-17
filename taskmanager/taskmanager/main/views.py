from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def index(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.order_by('id')
    # tasks = Task.objects.order_by('-title')
    # tasks = Task.objects.order_by('title')[:3]
    tasks = Task.objects.order_by('title')
    return render(request, 'main/index.html', {'title': "Главная страница", 'tasks': tasks})


def about(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'main/about.html', {'ip_address': ip})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Не верно заполненно"

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)
