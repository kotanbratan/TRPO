# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20160830_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер заявки'),
        ),
    ]
