# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20160612_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pic_name',
            field=models.CharField(default='default_life.png', max_length=20),
            preserve_default=True,
        ),
    ]
