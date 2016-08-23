# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160627_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('number', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('manager', models.CharField(max_length=200)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('product_model', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_partner',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_type',
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_partner',
            field=models.ForeignKey(to='myapp.Partner'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_product',
            field=models.ForeignKey(to='myapp.Product'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_status',
            field=models.ForeignKey(to='myapp.Status'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_type',
            field=models.ForeignKey(to='myapp.Type'),
        ),
    ]
