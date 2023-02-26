from django.contrib import admin
from .models import Project,Task

class TaskAdmin(admin.ModelAdmin): #create input with read only, in the dashboard admin
  readonly_fields = ('created', )
  
# Register your models here.
admin.site.register(Project) #see model with all CRUD in the dashboard admin
admin.site.register(Task, TaskAdmin) #see model with all CRUD in the dashboard admin