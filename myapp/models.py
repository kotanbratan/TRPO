from django.db import models
from django.utils import timezone

class Partner(models.Model):
    partner_name = models.CharField(max_length=100)
    partner_phone = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    product_model = models.CharField(max_length=100)

class Type(models.Model):
    type_name = models.CharField(max_length=100)

class Status(models.Model):
    status_name = models.CharField(max_length=100)

class Bid(models.Model):
    class Meta():
        db_table = 'Bid'
        
    number = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    manager = models.CharField(max_length=200)
    bid_partner = models.ForeignKey(Partner)
    bid_type = models.ForeignKey(Type)
    bid_product = models.ForeignKey(Product)
    amount = models.IntegerField(default=0)
    bid_status = models.ForeignKey(Status)
    total = models.IntegerField(default=0)
