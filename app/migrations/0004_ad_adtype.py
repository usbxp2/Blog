# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151204_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='adtype',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
    ]
