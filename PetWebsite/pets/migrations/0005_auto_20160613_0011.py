# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20160613_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='life_pic1',
            field=models.CharField(default='default.png', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='life_pic2',
            field=models.CharField(default='default.png', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='life_pic3',
            field=models.CharField(default='default.png', max_length=20),
            preserve_default=True,
        ),
    ]
