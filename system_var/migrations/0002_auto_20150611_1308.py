# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_var', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='var',
            options={'ordering': ['group', 'slug'], 'verbose_name': '\u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0430', 'verbose_name_plural': '\u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u044b'},
        ),
    ]
