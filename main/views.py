from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Status
from .forms import TaskFormCreate, TaskFormUpdate
from .config import column_names


def index(request):
    statuses_dict = {}
    for coloumn_name in column_names:
        statuses_dict[coloumn_name] = Task.objects.filter(status__name_status=coloumn_name)

    processed_data = [{'column_name': key, 'tasks': value} for key, value in statuses_dict.items()]
    return render(request, 'main/index.html', {'processed_data': processed_data})


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
    statuses = Status.objects.all()

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