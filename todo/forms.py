from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez une nouvelle tâche'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez une description de la tâche'}),
        }