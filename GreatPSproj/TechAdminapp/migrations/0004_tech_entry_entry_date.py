# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechAdminapp', '0003_tech_entry_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech_entry',
            name='entry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
