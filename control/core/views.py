from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView, TemplateView
from core.models import Task
from django.urls import reverse_lazy
from core.forms import TaskForm
from django.contrib import messages
import pandas as pd


class HomeView(TemplateView):
    template_name = 'core/home.html'

# Lista
class TaskListView(ListView):
    model = Task
    paginate_by = 10
    template_name = 'core/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = context['tasks']

        df = pd.DataFrame()





# Crear y actualizar
class TaskCreateView(CreateView):
    model = Task
    template_name = 'core/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('core:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class =TaskForm
    template_name = 'core/task_update.html'
    
    def form_valid(self, form):
        mensaje = 'Se ha modificado el registro'
        messages.add_message(self.request, messages.SUCCESS, mensaje)
        return super().form_valid(form)
       
    def get_success_url(self):
        return reverse_lazy('core:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'core/task_delete.html'
    success_url = reverse_lazy('core:task_list')



def toggle_task(request, task_id):
    task  = get_list_or_404(Task, id = task_id)
    task.estado = not task.estado
    task.save()
    return redirect('core:task_list')



