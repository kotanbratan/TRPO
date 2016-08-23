from django.conf.urls import patterns, include, url
from myapp import views
#from myapp.views import AuthView, BidsList, 

urlpatterns = [
    url(r'^$', views.bids_list, name='bids_list'),

]
