# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151202_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description2',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\xa0\x87\xe9\xa2\x982', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
    ]
