# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='building',
            field=models.ForeignKey(related_name='apartments_set', default=1, to='planing.Building'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=ckeditor.fields.RichTextField(default='<p>&nbsp;</p>', help_text='\u041f\u043b\u043e\u0449\u0430\u0434\u044c, \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043d\u0430\u0442 \u0438 \u0442.\u0434.', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=False,
        ),
    ]
