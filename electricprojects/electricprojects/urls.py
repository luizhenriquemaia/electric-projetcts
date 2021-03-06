from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('config/', include('config.urls')),
    path('client/', include('client.urls')),
    path('project/', include('project.urls')),
]
