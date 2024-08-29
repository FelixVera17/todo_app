from django import forms
from core.models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo','estado','accion','f_inicio','f_fin']
        widgets = {
            'f_inicio': forms.DateInput(attrs={'type': 'date'}),
            'f_fin': forms.DateInput(attrs={'type': 'date'}),
        }