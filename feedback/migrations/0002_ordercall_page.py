# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercall',
            name='page',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441\u0430\u0439\u0442\u0430', blank=True),
        ),
    ]
