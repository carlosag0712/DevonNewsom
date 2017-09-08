from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^friends$', views.friends),
    url(r'^(?P<friend>\w+)$', views.one_friend),    
]