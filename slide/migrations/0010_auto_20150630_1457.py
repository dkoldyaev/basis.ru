# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0009_slide_image_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title_line1_right',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line1_top',
            field=models.IntegerField(default=53),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line2_right',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line2_top',
            field=models.IntegerField(default=-40),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_width',
            field=models.IntegerField(default=350),
        ),
    ]
