# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160811_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
