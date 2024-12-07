
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('register_complaint', views.register_complaint, name='register'),
    path('track_complaint', views.track_complaint, name='track_complaint'),
]