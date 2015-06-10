# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0003_auto_20150610_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidepage',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
