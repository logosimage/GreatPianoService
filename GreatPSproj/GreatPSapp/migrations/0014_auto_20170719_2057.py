# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 03:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GreatPSapp', '0013_auto_20170719_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piano',
            old_name='request',
            new_name='service_request',
        ),
    ]