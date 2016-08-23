# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('manager', models.CharField(max_length=200)),
                ('total', models.IntegerField(default=0)),
                ('order_partner', models.ForeignKey(to='myapp.Partner')),
                ('order_status', models.ForeignKey(to='myapp.Status')),
                ('order_type', models.ForeignKey(to='myapp.Type')),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
