# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0008_auto_20170327_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='SumAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('time', models.CharField(max_length=256)),
                ('brief_time', models.CharField(max_length=256)),
            ],
        ),
    ]