# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20170504_0221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.RemoveField(
            model_name='member',
            name='test',
        ),
    ]
