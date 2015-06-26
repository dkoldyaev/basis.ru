# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0004_slidepage_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title_digit',
            field=models.CharField(help_text='\u0411\u043e\u043b\u044c\u0448\u0430\u044f \u0437\u0435\u043b\u0435\u043d\u0430\u044f \u0446\u0438\u0444\u0440\u0430', max_length=5, null=True, verbose_name='\u0426\u0438\u0444\u0440\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line1',
            field=models.CharField(help_text='\u041f\u0435\u0440\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u0430\u044f \u0447\u0443\u0442\u044c \u0432\u043b\u0435\u0432\u043e', max_length=50, null=True, verbose_name='\u0421\u0442\u043e\u043a\u0430 1', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line2',
            field=models.CharField(help_text='\u041f\u0435\u0440\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f, \u043f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u0430\u044f \u0447\u0443\u0442\u044c \u0432\u043f\u0440\u0430\u0432\u043e', max_length=50, null=True, verbose_name='\u0421\u0442\u043e\u043a\u0430 1', blank=True),
        ),
    ]
