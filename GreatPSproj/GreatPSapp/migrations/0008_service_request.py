# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreatPSapp', '0007_remove_piano_customerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]