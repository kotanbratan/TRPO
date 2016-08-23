# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_bid_amount'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bid',
            table='Bid',
        ),
    ]
