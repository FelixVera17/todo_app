from django.urls import path

from . import views

app_name  = 'core'


urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('task/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
