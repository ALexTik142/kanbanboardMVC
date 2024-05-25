from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                                         #Маршрут на главную страницу
    path('about-us', views.about, name='about'),                                #Маршрут на страницу о проекте
    path('create', views.create, name='create'),                                #Маршрут на добавление задачи
    path('task/<int:task_id>/update/', views.update_task, name='task-update'),  #Маршрут на изменение 1 задачи
    path('task/<int:task_id>/delete/', views.delete_task, name='task-delete')   #Маршрут на удаление 1 задачи
]
