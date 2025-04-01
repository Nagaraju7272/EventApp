"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("events.urls")),
    path("admin/", admin.site.urls),
    #path("events/", include("events.urls")),
]
