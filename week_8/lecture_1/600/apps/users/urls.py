from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register_view$', views.register_view),
    url(r'^login_view$', views.login_view),
    url(r'^success$', views.success),

    #CREW STUFF
    url(r'^create_crew$', views.create_crew),
    url(r'^join_crew$', views.join_crew),
]
