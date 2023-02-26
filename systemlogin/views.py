from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'GET':
        print(request.GET)
        print('obtaining data from the url = signup if it comes by GET')
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:
        print(request.POST)
        print('obtaining data from the url = signup if it comes by POST')
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')# this task is in the TESTAPP the other aplication
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})#resend the form and the error if it exists

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})#resend the form and the error if it exists
    
    
def home2(request):
    return render(request, 'home2.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home2')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')