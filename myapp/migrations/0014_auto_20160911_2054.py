# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_bid_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_partner',
            field=models.ForeignKey(blank=True, to='myapp.Partner', verbose_name='Контрагент', null=True),
        ),
    ]
