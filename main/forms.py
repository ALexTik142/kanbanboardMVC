from django import forms
from .models import Task


class TaskFormCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "deadline"]
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "deadline": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите дедлайн',
                'type': 'date'
            })
        }

        def __init__(self, *args, **kwargs):
            super(TaskFormCreate, self).__init__(*args, **kwargs)
            self.fields['deadline'].required = True


class TaskFormUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "deadline", "status"]
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "status": forms.Select(attrs={
                'class': 'form-control'
            }),
            "deadline": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите дедлайн',
                'type': 'date'
            })
        }