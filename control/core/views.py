from django.shortcuts import render, rever
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from core.models import Task
from django.urls import reverse_lazy
from core.forms import TaskForm


class HomeView(TemplateView):
    template_name= 'core/home.html'


#lista
class TaskListView(ListView):
    model = Task
    paginate_by = 10
    template_name = 'core/task_list.html'
    content_object_name = 'tasks'


#crear
class TaskFormMixin(CreateView,UpdateView):
    model = Task
    template_name = 'core/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('core:task_list')


class TaskCreateView(CreateView):
    pass


class TaskUpdateView(UpdateView):
    pass



class TaskDeleteView(DeleteView):
    model = Task
    template_name= 'core/task_delete.html'
    success_url = reverse_lazy('core:task_list')

#detail
class TaskDetailView(DetailView):
    model = Task
    template_name = 'core/task_detail.html'
    context_object_name = 'task'


