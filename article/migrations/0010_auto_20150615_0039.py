# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('article', '0009_auto_20150615_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='firstname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='lastname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
