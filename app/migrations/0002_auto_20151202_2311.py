# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='description2',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\x8f\x8f\xe8\xbf\xb02', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]
