from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from poll.models import Poll, Choice
from . import views


urlpatterns = [
    url(r'^$', views.new_poll, name='post_list'),
    url(r'^create_poll', views.create_poll, name='create_poll'),
]