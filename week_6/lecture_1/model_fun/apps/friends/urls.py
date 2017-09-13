from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create', views.create),

    # this will fetch a 'friend_id' (of any integer) that is passed to this pattern
    # so '/3' will send 3 to views.show as friend_id.  this will allow you to query 
    # Friend.objects.get(id=friend_id) and get back that partiuclar Friend
    url(r'^(?P<friend_id>\d+)', views.show)
]