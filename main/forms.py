from django import forms
from .models import Task


class TaskFormCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }


class TaskFormUpdate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "status"]
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
        }