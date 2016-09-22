# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151207_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='adtype',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'\xe9\xa1\xb6\xe9\x83\xa8\xe5\xb9\xbf\xe5\x91\x8a', 1), (b'\xe5\x8f\xb3\xe4\xbe\xa7\xe5\xb9\xbf\xe5\x91\x8a', 2)]),
        ),
    ]
