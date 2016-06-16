# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='life_pic1',
            field=models.CharField(max_length=20, default='default.png'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='life_pic2',
            field=models.CharField(max_length=20, default='default.png'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='life_pic3',
            field=models.CharField(max_length=20, default='default.png'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='region',
            field=models.CharField(max_length=15, default='北部'),
            preserve_default=True,
        ),
    ]
