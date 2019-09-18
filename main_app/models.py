from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.utils import timezone

class Group(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'group_id': self.id})


class Event(models.Model):
    title = models.CharField(max_length=250)
    # group = models.ManyToManyField(Group)
    location = models.URLField(max_length=250)
    description = models.TextField(max_length=250)
    # time = models.TimeField('time')
    # date = models.DateField('date')
    date = models.DateField()
    time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ManyToManyField(User)
    content = models.TextField(max_length=250)
