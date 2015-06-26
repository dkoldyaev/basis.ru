# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0005_auto_20150626_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='title_line1',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='title_line2',
        ),
    ]
