# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_interaction_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_user', to='backend.CustomUser'),
        ),
    ]
