# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 06:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publisged_date',
            new_name='published_date',
        ),
    ]
