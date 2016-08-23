from django.contrib import admin
from myapp.models import Bid, Partner, Status, Type, Product


#class BidAdmin(admin.ModelAdmin):
#    list_filter = ['date']

admin.site.register(Bid)#, BidAdmin)
#admin.site.register(Partner)
#admin.site.register(Status)
#admin.site.register(Type)
