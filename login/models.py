from django.db import models
import re
import datetime

class LoginManager(models.Manager):
   def validator(self, postData):
      errors = {}
      if len(postData['fname']) < 2 or not postData['fname'].isalpha():
         errors['fname'] = "First name should be only letters and at least 2 characters."
      if len(postData['lname']) < 2 or not postData['lname'].isalpha():
         errors['lname'] = "Last name should be only letters and at least 2 characters."
      bday = datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d").date()
      if bday > datetime.date.today():
         errors['lname'] = "You must have been born at least 13 years in the past to use this site."
      EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
      if not EMAIL_REGEX.match(postData['email']):           
         errors['email'] = "Email address is required and with proper A@B.XYZ format."  
      if User.objects.filter(email=postData['email']).exists():
         errors['emailreg'] = "The email address entered is already registered."
      if len(postData['password']) < 8:
         errors['passlength'] = "Password must be at least 8 characters."
      if postData['password'] != postData['p2']:
         errors['passmatch'] = "The password and confirmation password did not match."
      return errors

class User(models.Model):
   fname = models.CharField(max_length=255)
   lname = models.CharField(max_length=255)
   password = models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   birthday = models.DateField(null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   objects = LoginManager()

class Post(models.Model):
   postMessage = models.TextField()
   userid = models.ForeignKey(User, related_name="poster", on_delete = models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
   commentMessage = models.TextField()
   userid = models.ForeignKey(User, related_name="commenter", on_delete = models.CASCADE)
   postid = models.ForeignKey(Post, related_name="parentComment", on_delete = models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)