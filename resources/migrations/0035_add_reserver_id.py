# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0034_add_reserver_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reserver_id',
            field=models.CharField(blank=True, max_length=30, verbose_name='Reserver ID (business or person)'),
        ),
    ]