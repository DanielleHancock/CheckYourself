# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20160409_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='kit_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
