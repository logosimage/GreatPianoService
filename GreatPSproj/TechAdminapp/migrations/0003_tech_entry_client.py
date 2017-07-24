# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 04:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TechAdminapp', '0002_auto_20170722_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech_entry',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
