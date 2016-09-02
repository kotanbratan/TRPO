# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20160830_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Номер заявки'),
        ),
    ]
