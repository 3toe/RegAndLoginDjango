from django.urls import path     
from . import views

urlpatterns = [
   # GET method returning the index page render
   path('', views.index),

]