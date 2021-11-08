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
   path('success', views.success),
   # GET method logging the user out
   path('logout',  views.logout),
   # POST method to save post to DB
   path('postMessage', views.postMessage),
   # POST method to save comment to DB
   path('postComment/<int:sumnum>', views.postComment)
]