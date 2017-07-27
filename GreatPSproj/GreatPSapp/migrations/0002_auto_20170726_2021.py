# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreatPSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_request',
            name='appraisal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service_request',
            name='cleaning',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service_request',
            name='key_services',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service_request',
            name='regulation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service_request',
            name='repair',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service_request',
            name='tune',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]