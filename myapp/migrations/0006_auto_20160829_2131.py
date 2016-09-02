# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160811_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'verbose_name_plural': 'Заявки', 'verbose_name': 'Заявка'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name_plural': 'Контрагенты', 'verbose_name': 'Контрагент'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Товары', 'verbose_name': 'Товар'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Статусы', 'verbose_name': 'Статус'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name_plural': 'Типы', 'verbose_name': 'Тип'},
        ),
        migrations.RemoveField(
            model_name='bid',
            name='total',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_model',
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_partner',
            field=models.ForeignKey(to='myapp.Partner', verbose_name='Контрагент'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_product',
            field=models.ForeignKey(to='myapp.Product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_status',
            field=models.ForeignKey(to='myapp.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_type',
            field=models.ForeignKey(to='myapp.Type', verbose_name='Тип заявки'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='manager',
            field=models.CharField(max_length=200, verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер заявки'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='organization',
            field=models.CharField(max_length=200, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_name',
            field=models.CharField(max_length=100, verbose_name='Имя контрагента'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_name',
            field=models.CharField(max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(max_length=100, verbose_name='Тип заявки'),
        ),
        migrations.AlterModelTable(
            name='bid',
            table=None,
        ),
    ]
