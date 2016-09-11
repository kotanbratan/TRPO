from django.conf.urls import patterns, include, url
from myapp import views
#from myapp.views import MainView, temp#, AuthView, BidsList

urlpatterns = [
    url(r'^$', views.MainView, name='main'),
    url(r'^1/', views.temp_one),
    url(r'^2/', views.temp_two),
    url(r'^3/', views.temp_three),
    url(r'^bids/all/$', views.BidsList),
    url(r'^bid/(?P<pk>\d+)/$', views.BidView, name = "bid"),
    url(r'^products/all/$', views.ProductsList),
    url(r'^partners/all/$', views.PartnersList),
    url(r'^bid/(?P<pk>\d+)/edit/$', views.BidEditView, name = 'bid_edit'),
    url(r'^bid/(?P<pk>\d+)/status/$', views.StatusEdit),
    #url(r'^bid/(?P<bid_id>\d+)/status/new/$', views.NewBidView),
    #url(r'^bid/(?P<bid_id>\d+)/edit/new/$', views.NewBidView),
    url(r'^bid/new/$', views.NewBidView, name = 'bid_new'),
    #url(r'^auth/$', views.AuthView, name='auth'),
]
