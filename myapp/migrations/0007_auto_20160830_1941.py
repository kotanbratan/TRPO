# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20160829_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bid_partner',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bid_product',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bid_status',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bid_type',
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Заявки', 'verbose_name': 'Заявка'},
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
