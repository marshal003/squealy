# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-02 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squealy', '0004_auto_20170331_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='dropdown_api',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
