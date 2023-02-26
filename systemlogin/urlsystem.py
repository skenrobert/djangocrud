from django.urls import path
from . import views # that dot points to the root of this file

urlpatterns = [
    # path('system', views.home, name=""),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('home2', views.home2, name="home2"),
]