"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from django.urls import path
from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("add/", views.add_events, name="add_events"),
    path("past/", views.past_events, name="past_events"),
    path("view/<int:event_id>/", views.view_events, name="view_events"),
    path("register/<int:event_id>/", views.register_events, name="register_events"),
    path("edit/<int:event_id>/", views.edit_events, name="edit_events"),
    path("cancel/<int:event_id>/", views.cancel_events, name="cancel_events"),
    path("my/", views.my_events, name="my_events"),
]
