# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0002_slide_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ['order'], 'verbose_name': '\u0421\u043b\u0430\u0439\u0434', 'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b'},
        ),
        migrations.AlterModelOptions(
            name='slidepage',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0441\u043b\u0430\u0439\u0434\u043e\u0432', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0441\u043b\u0430\u0439\u0434\u043e\u0432'},
        ),
        migrations.AddField(
            model_name='slide',
            name='order',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
    ]
