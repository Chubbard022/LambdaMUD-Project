"""
Routes for registration. These routes give a user a token when they have been authorized
"""

from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
