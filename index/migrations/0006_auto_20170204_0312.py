# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-03 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20170204_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='link',
            field=models.CharField(default='VbSsim', max_length=40),
        ),
    ]
