from django import forms
from todolist.models import Task

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
        ]