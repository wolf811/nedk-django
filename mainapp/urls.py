from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
]
