# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='page',
            field=models.ForeignKey(related_name='slide_set', default=1, to='slide.SlidePage'),
            preserve_default=False,
        ),
    ]
