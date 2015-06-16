# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import article.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(upload_to=article.models.get_upload_file_name),
        ),
    ]
