from django.urls import path
from . import views # that dot points to the root of this file

urlpatterns = [
    path('', views.home, name=""),
    path('about', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('showprojects', views.showprojects),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('showtasks/<int:id>', views.showtasks),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('projects', views.projects, name="projects"),
    path('tasks', views.tasks, name="tasks"),
    path('create_task', views.create_task, name="create_task"),
    path('create_project', views.create_project, name="create_project"),
]