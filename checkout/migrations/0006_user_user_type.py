# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20160324_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('STAFF', 'Staff'), ('STUDENT', 'Student')], default='STUDENT', max_length=7),
        ),
    ]