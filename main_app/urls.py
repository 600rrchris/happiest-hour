from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('groups/', views.groups_index, name='groups'),
    path('accounts/signup', views.signup, name='signup'),
    path('events/index', views.events_index, name='events_index'),
    path('events/new', views.EventCreate.as_view(), name='events_new'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('events/details', views.events_details, name='events_details'),
    path('groups/details', views.groups_details, name='groups_details'),
    path('groups/new', views.GroupCreate.as_view(), name='groups_new'),
    path('groups/<int:pk>/update', views.GroupUpdate.as_view(), name='groups_update'),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='groups_delete'),
    path('groups/index', views.groups_index, name='groups_index'),
]