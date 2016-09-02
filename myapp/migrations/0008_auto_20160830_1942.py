# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20160830_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.IntegerField(default=0, verbose_name='Номер заявки')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('manager', models.CharField(max_length=200, verbose_name='Менеджер')),
                ('amount', models.IntegerField(default=0, verbose_name='Количество')),
                ('bid_partner', models.ForeignKey(to='myapp.Partner', verbose_name='Контрагент')),
                ('bid_product', models.ForeignKey(to='myapp.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'verbose_name': 'Заявка',
            },
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Статусы', 'verbose_name': 'Статус'},
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_status',
            field=models.ForeignKey(to='myapp.Status', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_type',
            field=models.ForeignKey(to='myapp.Type', verbose_name='Тип заявки'),
        ),
    ]
