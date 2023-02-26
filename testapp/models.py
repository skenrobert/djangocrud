from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)# size text or save empty
    done = models.BooleanField(default=False) #Upper case this value
    created = models.DateTimeField(auto_now_add=True) #date with create task
    datecompleted = models.DateTimeField(null=True, blank=True)# nullable or save empty
    important = models.BooleanField(default=False)# bool 
    user = models.ForeignKey(User, on_delete=models.CASCADE)# foreignkey (import for Django)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)# foreignkey (create behind)
    
    def __str__(self):
         return self.title + ' - ' + self.user.username #use from dashboard admin, the user with create task, is show of form= titletask - username
    
    # def __str__(self):
    #     return self.title +'-'+ self.project.name