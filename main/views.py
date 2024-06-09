from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Status
from .forms import TaskFormCreate, TaskFormUpdate


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskFormCreate()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    statuses = Status.objects.all()  # Предполагается, что у вас есть модель Status

    if request.method == 'POST':
        form = TaskFormUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskFormUpdate(instance=task)

    return render(request, 'main/update.html', {'form': form, 'task': task, 'statuses': statuses})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')