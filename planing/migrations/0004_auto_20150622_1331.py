# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0003_auto_20150610_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='plan_fill',
            field=models.FileField(upload_to=b'apartment/plan_fill', null=True, verbose_name='\u0417\u0430\u043b\u0438\u0432\u043a\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438'),
        ),
        migrations.AddField(
            model_name='building',
            name='plan',
            field=models.FileField(upload_to=b'building/plan', null=True, verbose_name='\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u043a\u0430 \u044d\u0442\u0430\u0436\u0430'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='plan',
            field=models.FileField(upload_to=b'apartment/plan', null=True, verbose_name='\u041f\u043b\u0430\u043d \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b'),
        ),
    ]
