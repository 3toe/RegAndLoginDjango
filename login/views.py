from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# GET method returning the index page render
def index(request):
   return render(request, 'index.html')

# POST method for the registration, with an if for success/fail
def reg(request):
   errors = User.objects.validator(request.POST)
   if len(errors) > 0:
      for key, value in errors.items():
         messages.error(request, value)
      return redirect('/')
   pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
   User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], password = pw_hash, email = request.POST['email'])
   user = User.objects.filter(email=request.POST['email'])
   if user:
      logged_in = user[0]
      request.session['fname'] = logged_in.fname
   return redirect('/success')

# POST method for the login, with an if for success/fail
def login(request):
   user = User.objects.filter(email=request.POST['email'])
   if user:
      logged_in = user[0]
      if bcrypt.checkpw(request.POST['password'].encode(), logged_in.password.encode()):
         request.session['fname'] = logged_in.fname
         return redirect('/success')
   messages.error(request, "Your username or password is incorrect.")
   return redirect('/')

def logout(request):
   request.session.flush()
   return redirect('/')

# GET method rendering the successful registration/login page
def success(request):
   if not 'fname' in request.session:
      return redirect('/')
   return render(request, 'success.html')