# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
