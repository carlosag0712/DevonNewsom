from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^new$", views.new),
    url(r"^create$", views.create),
    url(r'^(?P<artist_id>\d+)$', views.show),
    url(r'^(?P<artist_id>\d+)/delete$', views.delete)
]