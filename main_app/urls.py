from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('groups/', views.groups_index, name='groups'),
    path('accounts/signup', views.signup, name='signup'),
    path('events/index', views.events_index, name='events_index'),
    path('events/new', views.events_new, name='events_new'),
    path('events/details', views.events_details, name='events_details')
]
