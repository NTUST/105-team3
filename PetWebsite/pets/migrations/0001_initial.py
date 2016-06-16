# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=15)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('sterilization', models.BooleanField(default=False)),
                ('health', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=100)),
                ('pic_name', models.CharField(default='default.png', max_length=20)),
                ('contact', models.ForeignKey(to='pets.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
