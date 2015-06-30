# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0007_auto_20150626_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image_position',
            field=models.CharField(default=b'0% 0%', max_length=255, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'),
        ),
    ]
