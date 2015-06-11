# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150610_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='announce',
            field=models.TextField(help_text='\u0411\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439', verbose_name='\u0410\u043d\u043e\u043d\u0441'),
        ),
    ]
