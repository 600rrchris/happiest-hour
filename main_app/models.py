from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)

class Group(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=250)

class Event(models.Model):
    title : models.CharField(max_length=250)
    group : models.ManyToManyField(Group)
    location : models.URLField(max_length=200)
    time :  models.TimeField(auto_now=False, auto_now_add=False,)
    date : models.DateField(auto_now=False, auto_now_add=False,)

class Comment(models.Model):
    user : models.ManyToManyField(User)
    content: models.TextField(max_length=250)