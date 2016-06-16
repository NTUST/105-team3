# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_auto_20160613_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='life_pic1',
            field=models.CharField(max_length=50, default='default.png'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='life_pic2',
            field=models.CharField(max_length=50, default='default.png'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='life_pic3',
            field=models.CharField(max_length=50, default='default.png'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='pic_name',
            field=models.CharField(max_length=50, default='default.png'),
            preserve_default=True,
        ),
    ]
