# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0006_auto_20150626_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title_line1_deg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line1_text',
            field=ckeditor.fields.RichTextField(help_text='\u041f\u0435\u0440\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f', max_length=50, null=True, verbose_name='\u0421\u0442\u0440\u043e\u043a\u0430 1', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line2_deg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_line2_text',
            field=ckeditor.fields.RichTextField(help_text='\u0412\u0442\u043e\u0440\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f', max_length=50, null=True, verbose_name='\u0421\u0442\u0440\u043e\u043a\u0430 2', blank=True),
        ),
    ]
