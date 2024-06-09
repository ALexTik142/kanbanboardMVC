from django.db import models


class Status(models.Model):
    name_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name_status


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'