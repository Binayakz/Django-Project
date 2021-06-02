from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    tasks = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'id': 'todoField', 'placeholder': 'Enter Task'
    }))

    class Meta:
        model = Todo
        fields = ['tasks', ]
