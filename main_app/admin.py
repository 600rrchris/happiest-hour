from django.contrib import admin
from .models import Group, User, Comment, Event
# Register your models here.
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Event)
