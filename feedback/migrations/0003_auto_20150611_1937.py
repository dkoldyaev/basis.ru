# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_ordercall_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercall',
            name='phone',
            field=models.CharField(default=' ', max_length=255, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=False,
        ),
    ]
