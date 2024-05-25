from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    #Регаем маршруты приложения
    path('', include('main.urls'))   #Перенаправляем их на другой файл в main.urls
]