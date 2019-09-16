from django.contrib import admin
from .models import Group, User, Comment, Event, Poll
# Register your models here.
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Poll)

