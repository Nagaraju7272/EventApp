from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("events.urls")),
    
    path("admin/", admin.site.urls),
    #path("events/", include("events.urls")),
]
