# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import article.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20150613_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default='', upload_to=article.models.get_upload_file_name),
        ),
    ]
