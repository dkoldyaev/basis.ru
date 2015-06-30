# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0008_slide_image_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image_size',
            field=models.CharField(default=b'100% 100%', max_length=255, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'),
        ),
    ]
