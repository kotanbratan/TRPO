# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20160911_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_product',
            field=models.ForeignKey(null=True, verbose_name='Товар', blank=True, to='myapp.Product'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_status',
            field=models.ForeignKey(null=True, verbose_name='Статус', blank=True, to='myapp.Status'),
        ),
    ]
