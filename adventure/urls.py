"""
These urlpatterns are the endpoints that the frontend is hitting to do the following
--initialize the world
--initialize the player
--say something within a room to other players
--update the player move and making sure the next move is legal
"""

from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('map', api.map)
]