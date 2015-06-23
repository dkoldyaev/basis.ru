# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0004_auto_20150622_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='plan_fill_area',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u043e\u0431\u043b\u0430\u0441\u0442\u0438', blank=True),
        ),
    ]
