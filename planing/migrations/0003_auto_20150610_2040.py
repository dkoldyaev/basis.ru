# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0002_auto_20150610_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'ordering': ['order'], 'verbose_name': '\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u043a\u0430 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b', 'verbose_name_plural': '\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u043a\u0438 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['order'], 'verbose_name': '\u0414\u043e\u043c', 'verbose_name_plural': '\u0414\u043e\u043c\u0430'},
        ),
        migrations.AddField(
            model_name='apartment',
            name='order',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='building',
            name='order',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
    ]
