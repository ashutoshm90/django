# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def split_names(apps, schema_editor):
    comment = apps.get_model("article", "comment")
    for comment in comment.objects.all():
        try:
            comment.firstname, comment.lastname = comment.name.split(" ")
        except:
            comment.firstname, comment.lastname = comment.name, " "
        comment.save()

def clear_data(apps, schema_editor):
    comment = apps.get_model("article", "comment")
    for comment in comment.objects.all():
        comment.name = ""
        comment.save()

class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20150615_0039'),
    ]

    operations = [
        migrations.RunPython(split_names),
        migrations.RunPython(clear_data),
    ]
