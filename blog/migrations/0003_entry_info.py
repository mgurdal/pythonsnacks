# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160427_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='info',
            field=models.CharField(default='Blog Post', max_length=140),
            preserve_default=False,
        ),
    ]