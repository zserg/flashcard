# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='easiness',
            field=models.FloatField(default=2.5),
        ),
    ]
