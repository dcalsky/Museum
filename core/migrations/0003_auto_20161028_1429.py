# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 06:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161026_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=160)),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2016, 10, 28, 14, 29, 51, 983310))),
            ],
            options={
                'ordering': ['create_time'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 28, 14, 29, 51, 981551)),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]