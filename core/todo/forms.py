from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "name" : "title",
                "placeholder" : "Task title",
            }
        ),
        label="",
    )

    class Meta:
        model = Task
        fields = ('title',)