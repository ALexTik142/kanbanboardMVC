from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def index(request): #Представление для перенаправления на главную страницу
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request): #Представление для перенаправления на страницу о нас
    return render(request, 'main/about.html')


def create(request):    #Представление для добавления 1 задачи
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Создаем экземпляр задачи, но не сохраняем в базу данных
            task.user = request.user  # Присваиваем текущего пользователя задаче
            task.save()  # Сохраняем задачу в базе данных
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def update_task(request, task_id):  #Представление для изменения 1 задачи
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = TaskForm(instance=task)

    return render(request, 'main/update.html', {'form': form, 'task': task})


def delete_task(request, task_id):  #Представление для удаления 1 задачи
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')  # Перенаправляем на главную страницу