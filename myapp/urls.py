from django.conf.urls import patterns, include, url
from myapp import views
#from myapp.views import MainView, temp#, AuthView, BidsList

urlpatterns = [
    url(r'^$', views.MainView, name='main'),
    url(r'^1/', views.temp_one),
    url(r'^2/', views.temp_two),
    url(r'^3/', views.temp_three),
    url(r'^bids/all/$', views.bids),
    url(r'^bid/(?P<bid_id>\d+)/$', views.bid),
    #url(r'^auth/$', views.AuthView, name='auth'),
    #url(r'^bids/$', views.BidsListView, name='bids_list'),
]
