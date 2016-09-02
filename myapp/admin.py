from django.contrib import admin
from myapp.models import Bid, Partner, Status, Type, Product
from django.contrib.admin import ModelAdmin


class BidAdmin(ModelAdmin):
    list_filter = ['date']
    list_display = ('id', 'date', 'bid_partner', 'bid_product', 'amount')
    fieldsets = [
        ('Общая информация о заявке', {'fields': ['date', 'bid_type', 'bid_status', 'manager', 'bid_partner']}),
        ('Информация о товарах', {'fields': ['bid_product', 'amount']}),]

class ProductAdmin(ModelAdmin):
    list_filter = ['product_name']
    list_display = ('product_name', 'price')

class PartnerAdmin(ModelAdmin):
    list_display = ('partner_name', 'partner_phone')

class StatusAdmin(ModelAdmin):
    list_display = ('status_name',)

class TypeAdmin(ModelAdmin):
    list_display = ('type_name',)


admin.site.register(Bid, BidAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Product, ProductAdmin)
