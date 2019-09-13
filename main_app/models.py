from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    title : models.CharField(max_length=250)
    group : models.ManyToManyField(Group)
    location : models.URLField(max_length=200)
    time :  models.TimeField(auto_now=False, auto_now_add=False,)
    date : models.DateField(auto_now=False, auto_now_add=False,)

class Comment(models.Model):
    user : models.ManyToManyField(User)
    content: models.TextField(max_length=250)