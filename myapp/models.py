from django.db import models
from django.utils import timezone


class Partner(models.Model):
    partner_name = models.CharField("Имя контрагента", max_length=100)
    partner_phone = models.IntegerField("Телефон", blank=True, null=True)
    organization = models.CharField("Организация", max_length=200)

    class Meta():
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"

    def __str__(self):
        return self.partner_name



class Product(models.Model):
    product_name = models.CharField("Наименование", max_length=100)
    price = models.IntegerField("Цена", default=0)

    class Meta():
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.product_name



class Type(models.Model):
    type_name = models.CharField("Тип заявки", max_length=100)

    class Meta():
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.type_name



class Status(models.Model):
    status_name = models.CharField("Статус", max_length=100)

    class Meta():
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.status_name



class Bid(models.Model):
    date = models.DateTimeField("Дата", default=timezone.now)
    manager = models.CharField("Менеджер", max_length=200)
    bid_partner = models.ForeignKey(Partner, verbose_name="Контрагент", null=True, blank=True)
    bid_type = models.ForeignKey(Type, verbose_name="Тип заявки", null=True, blank=True)
    bid_product = models.ForeignKey(Product, verbose_name="Товар", null=True, blank=True)
    amount = models.IntegerField("Количество", default=0)
    bid_status = models.ForeignKey(Status, verbose_name="Статус", null=True, blank=True)

    def __unicode__(self):
        return self.manager

    def __str__(self):
        return self.manager

    def get_bid_partner(self):
        return self.bid_partner

    def get_bid_type(self):
        return self.bid_type

    def get_bid_product(self):
        return self.bid_product

    def get_bid_status(self):
        return self.bid_status

    class Meta():
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
