from django.conf.urls import patterns, include, url
from django.contrib import admin
import myapp

admin.autodiscover()

urlpatterns = [

    #url(r'^admin/', include('admin.site.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('myapp.urls','myapp')),
]
