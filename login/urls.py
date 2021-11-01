from django.urls import path     
from . import views

urlpatterns = [
   # GET method returning the index page render
   path('', views.index),
   # POST method for the registration
   path('reg',  views.reg),
   # POST method for the login
   path('login',  views.login),
   # GET method rendering the successful registration/login page
   path('success', views.success)
]