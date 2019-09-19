from django.db import models 
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_db(password)
        user.save(user=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True )
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email + ', ' + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    

class Group(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(Account)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups_details', kwargs={'group_id': self.id})
    

class Comment(models.Model):
    user = models.ManyToManyField(Account)
    content = models.TextField(max_length=250)
    
    
    
    
class Event(models.Model):
    title = models.CharField(max_length=250)
    group = models.ManyToManyField(Group)
    location = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now=False)


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





