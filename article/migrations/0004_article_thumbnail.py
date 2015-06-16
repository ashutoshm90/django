# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import article.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=datetime.datetime(2015, 6, 13, 16, 4, 19, 259041, tzinfo=utc), upload_to=article.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
