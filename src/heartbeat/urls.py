from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='hbindex'),
    url(r'^details/$', views.details, name='hbdetails'),
]
