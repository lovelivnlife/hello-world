"""Defines URL patterns for eLearn."""

from django.urls import path
from . import views

app_name = "eLearn"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
]
