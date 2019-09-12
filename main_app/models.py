from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)

class Group(models.Model):
    user = models.ManyToManyRel(User)
    name = models.CharField(max_length=250)

class Event(models.Model):
    title : models.CharField(max_length=250)
    group : models.ManyToOneRel(Group)
    location : models.URLField(max_length=200)
    time :  models.TimeField(auto_now=False, auto_now_add=False,)
    date : models.DateField(auto_now=False, auto_now_add=False,)

class Comments(models.Model):
    user : models.OneToOneRel(User)
    content: models.TextField(?)