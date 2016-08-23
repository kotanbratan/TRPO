from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.bids_list, name='bids_list'),

]
