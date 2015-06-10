# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['date'], 'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
