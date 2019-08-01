"""
These endpoints also associate to the other endpoints within the adventure file.
The frontend will use these endpoints and then include the other endpoints to 
the end of it to receive particular data they need.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
]
