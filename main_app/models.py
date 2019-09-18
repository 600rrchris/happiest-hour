from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.utils import timezone

class Group(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'group_id': self.id})
    

class Comment(models.Model):
    user = models.ManyToManyField(User)
    content = models.TextField(max_length=250)
    
    
class Event(models.Model):
    title = models.CharField(max_length=250)
    # group = models.ManyToManyField(Group)
    location = models.URLField(max_length=250)
    description = models.TextField(max_length=250)
    # time = models.TimeField('time')
    # time = models.TimeField(auto_now=False, auto_now_add=False,)
    # date = models.DateField('date')
    # date = models.DateField(auto_now=False, auto_now_add=False,)
    date = models.DateField()
    time = models.DateTimeField(auto_now_add=True)


# Creates poll form within events 
class Poll(models.Model):
    location_name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %d polls' % (self.location_name, self.count)

    @classmethod
    def bulk_poll(cls, location_names):
        with transaction.atomic():
            for location_name in location_names:
                if len(location_name) == 0:
                    continue

                if Poll.objects.filter(location_name=location_name).exists():
                    Poll.objects.filter(location_name=location_name).update(count=models.F('count') + 1)
                else:
                    Poll.objects.create(location_name=location_name, count=1)





