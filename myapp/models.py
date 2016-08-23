from django.db import models
from django.utils import timezone

class Partner(models.Model):
    partner_name = models.CharField("Имя контрагента", max_length=100)
    partner_phone = models.IntegerField("Телефон", blank=True, null=True)
    organization = models.CharField("Организация", max_length=200)

    class Meta():
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"

class Product(models.Model):
    product_name = models.CharField("Наименование", max_length=100)
    price = models.IntegerField("Цена", default=0)
    product_model = models.CharField("Модель", max_length=100)

    class Meta():
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Type(models.Model):
    type_name = models.CharField("Тип заявки", max_length=100)

class Status(models.Model):
    status_name = models.CharField("Статус", max_length=100)

class Bid(models.Model):
    number = models.IntegerField("Номер заявки", default=0)
    date = models.DateTimeField("Дата", default=timezone.now)
    manager = models.CharField("Менеджер", max_length=200)
    bid_partner = models.ForeignKey(Partner, verbose_name="Контрагент")
    bid_type = models.ForeignKey(Type, verbose_name="Тип заявки")
    bid_product = models.ForeignKey(Product, verbose_name="Товар")
    amount = models.IntegerField("Количество", default=0)
    bid_status = models.ForeignKey(Status, verbose_name="Статус")
    #total = models.IntegerField("Сумма", default=0)

    class Meta():
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
