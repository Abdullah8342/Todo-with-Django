from django import forms
from .models import Todo

class FormTodo(forms.ModelForm):


    class Meta:
        model = Todo
        fields = ['title','description','todo_status']
