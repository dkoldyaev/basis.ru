# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150610_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(help_text='\u0411\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u043d\u0430\u0434 \u0442\u0435\u043a\u0441\u0442\u043e\u043c \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0439 \u043d\u043e\u0432\u043e\u0441\u0442\u0438', upload_to=b'news/image', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
    ]
