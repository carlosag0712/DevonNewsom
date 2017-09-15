from django.conf.urls import url
from . import views

urlpatterns = [
    # Read all Actors
    url(r'^$', views.index),
    url(r'^filter$', views.filtered),
    # Read a single Actor
    url(r'^(?P<actor_id>\d+)$', views.show),
    # New template for Actor
    url(r'^new$', views.new),
    # Create an Actor
    url(r'^create$', views.create),
    # Edit an Actor
    # Update an Actor
    url(r'^destroy/(?P<actor_id>\d+)$', views.destroy),
    # Destroy an Actor
]