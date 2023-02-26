# djangocrud
 
this project is a basic example in django.

1) I need install python first, them check version (commando below is verifit good funtionation python and what version you install)

check version 
python3 --version
pip --version

2) first create folder (name project) them in cmd run the following command
pip install virtualenv

check version:
virtualenv - -version 

create virtual environment(this is a good practice, python work better each projects during development, allows to have different environments):
virtualenv venv

3) activate virtual environment(in windows, these environments are recommended to be able to work different versions of python on the same computer and framework):
.\venv\Scripts\activate  (for exit write: deactivate)

4) vcode note:
search folder and drag in visual code them press f1 select version python with star 
then press f1 write create new terminal (in this way the terminal will be executed from the root of python)

5) install django:

pip install django

django-admin - -version
or
python -m django - -version

6) create project:  (best option no create new folder outside, same level venv)

django-admin startproject myapp

7) execute server: default address http://127.0.0.1:8000/

python manage.py runserver

8) all command
python manage.py - -help

9) django works by default with small applications called app how to create each application and then integrate into the main one

python manage.py startapp testapp

#note:
#configuration project file is settings.py
#configuration starapp file is apps.py

10)#install sqlite Graphic interface (default database with python)
https://sqlitebrowser.org/

#note: press key f5 in application portable sqlite after run migration in terminal python

11) make file migration (default migration)
python manage.py makemigrations

#execute all migration
python manage.py migrate

#create first model in this route:  \djangoproject\testapp\models.py

class Project(models.Model):
    name = models.CharField(max_length=200)

#execute migration specific(model specific) 
python manage.py makemigrations testapp
 
#after
python manage.py makemigrations testapp
#them
python manage.py migrate testapp

#note: configuration other database (default sqlite)
#https://docs.djangoproject.com/en/4.1/ref/databases/

12) for into in http://127.0.0.1:8000/admin (first create user in shell the python)
python manage.py createsuperuser

note: manager models from admin, should change file in this route
\djangoproject\testapp\admin.py

from .models import Task

admin.site.register(Task)

