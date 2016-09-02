# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20160830_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='number',
            field=models.TextField(verbose_name='Номер заявки'),
        ),
    ]
