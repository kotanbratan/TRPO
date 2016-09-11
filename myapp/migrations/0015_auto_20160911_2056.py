# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20160911_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_type',
            field=models.ForeignKey(null=True, verbose_name='Тип заявки', to='myapp.Type', blank=True),
        ),
    ]
