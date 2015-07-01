# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0010_auto_20150630_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidepage',
            name='pie_menu',
            field=models.BooleanField(default=False, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u0440\u0443\u0433\u043e\u0432\u043e\u0439 \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u044c \u0441\u043b\u0430\u0439\u0434\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_line2_top',
            field=models.IntegerField(default=-45),
        ),
    ]
