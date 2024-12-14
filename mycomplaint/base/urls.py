
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('register_complaint', views.register_complaint, name='register'),
    path('track_complaint', views.track_complaint, name='track_complaint'),
    path('view_complaint', views.view_complaint, name='view_complaint'),

    path('facultyhome', views.facultyhome, name='facultyhome'),
    path('notifications', views.notifications, name='notifications'),
    path('new_complaints', views.new_complaints, name='new_complaints'),
    path('pending_complaints', views.pending_complaints, name='pending_complaints'),
    path('resolved_complaints', views.resolved_complaints, name='resolved_complaints'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
]