# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20150706_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(upload_to=b'contacts/contact/image', null=True, verbose_name='\u0424\u043e\u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
    ]
