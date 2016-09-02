# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20160831_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='number',
        ),
    ]
