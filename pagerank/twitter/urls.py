from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.twitter_graph, name='twitter_graph'),
]