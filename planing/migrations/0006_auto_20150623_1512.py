# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0005_apartment_plan_fill_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='\u041f\u043b\u043e\u0449\u0430\u0434\u044c, \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043d\u0430\u0442 \u0438 \u0442.\u0434.', null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.IntegerField(null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0437\u0430 \u043c\xb2', blank=True),
        ),
    ]
