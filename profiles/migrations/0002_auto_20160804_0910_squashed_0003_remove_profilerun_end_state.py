# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-08-04 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'profiles', '0002_auto_20160804_0910'), (b'profiles', '0003_remove_profilerun_end_state')]

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilerun',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
