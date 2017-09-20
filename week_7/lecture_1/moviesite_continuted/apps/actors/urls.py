from django.conf.urls import url
from . import views

urlpatterns = [
    # Read all Actors
    url(r'^$', views.index),
    url(r'^filter$', views.filtered),
    # Read a single Actor
    url(r'^actor/(?P<actor_id>\d+)$', views.show),
    url(r'^actor/(?P<actor_id>\d+)/addfilm$', views.add_to_filmog),
    # New template for Actor
    url(r'^new$', views.new),
    # Create an Actor
    url(r'^create$', views.create),
    url(r'^movies/create', views.create_movie),
    url(r'^movies/new', views.new_movie),
    # Edit an Actor
    # Update an Actor
    url(r'^destroy/(?P<actor_id>\d+)$', views.destroy),
    # Destroy an Actor
]