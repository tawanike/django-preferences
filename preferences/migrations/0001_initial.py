# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-03 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sites', models.ManyToManyField(blank=True, null=True, to='sites.Site')),
            ],
        ),
    ]
