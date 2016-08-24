from django.conf.urls import patterns, include, url
from myapp import views
#from myapp.views import MainView, AuthView, BidsList,

urlpatterns = [
    url(r'^$', views.MainView, name='main'),
    url(r'^auth/$', views.AuthView, name='auth'),
    url(r'^bids/$', views.BidsListView, name='bids_list'),
]
