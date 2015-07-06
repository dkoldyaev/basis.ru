# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='map_code',
        ),
        migrations.AddField(
            model_name='contact',
            name='coord',
            field=models.CharField(default='56.5068332, 60.8434739', max_length=255, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u043c\u0430\u0440\u043a\u0435\u0440\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='coord_popup',
            field=ckeditor.fields.RichTextField(default='\u0433. \u0421\u044b\u0441\u0435\u0440\u0442\u044c, \u0443\u043b.\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u0435\u0439., \u0434. 8 \u0441\u0442\u0440. 1<br/>\u041c\u0424\u041a <\u0413\u043e\u0440\u043e\u0434 \u0411\u0430\u0437\u0438\u0441>', verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0432\u0441\u043f\u043b\u044b\u0432\u0430\u044e\u0449\u0435\u0439 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0435 \u043c\u0430\u0440\u043a\u0435\u0440\u0430'),
            preserve_default=False,
        ),
    ]
