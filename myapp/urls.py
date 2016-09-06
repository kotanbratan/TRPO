from django.conf.urls import patterns, include, url
from myapp import views
#from myapp.views import MainView, temp#, AuthView, BidsList

urlpatterns = [
    url(r'^$', views.MainView, name='main'),
    url(r'^1/', views.temp_one),
    url(r'^2/', views.temp_two),
    url(r'^3/', views.temp_three),
    url(r'^bids/all/$', views.BidsList),
    url(r'^bid/(?P<bid_id>\d+)/$', views.BidView),
    url(r'^products/all/$', views.ProductsList),
    #url(r'^bid/edit/(?P<bid_id>\d+)/$', views.bid_edit),
    url(r'^partners/all/$', views.PartnersList),
    #url(r'^bid/status/(?P<bid_id>\d+)/$', views.bid_status_edit),

    #url(r'^auth/$', views.AuthView, name='auth'),
]
