# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0006_auto_20170719_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customerID',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]