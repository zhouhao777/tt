# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttapp', '0008_delete_crawler'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicID', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=100)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
