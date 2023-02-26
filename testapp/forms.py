from django import forms
from django.forms import ModelForm
from .models import Task

# class CreateNewTask(forms.Form):
#     title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
#     description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    
class CreateNewTask(ModelForm): #form advanced for create forms
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyect", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))