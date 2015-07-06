# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('menu', '0002_auto_20150610_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='headermenuitem',
            name='contacts_contact',
            field=models.ForeignKey(blank=True, to='contacts.Contact', null=True),
        ),
    ]
