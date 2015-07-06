# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_headermenuitem_contacts_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headermenuitem',
            name='type',
            field=models.CharField(default=b'page', help_text='\u041a\u0430\u043a\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u043e\u0442\u043a\u0440\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043f\u043e \u043a\u043b\u0438\u043a\u0443 \u043d\u0430 \u043f\u0443\u043d\u043a\u0442 \u043c\u0435\u043d\u044e', max_length=255, verbose_name='\u0422\u0438\u043f', choices=[(b'slide_page', '\u0413\u0440\u0443\u043f\u043f\u0430 \u0441\u043b\u0430\u0439\u0434\u043e\u0432'), (b'news_list', '\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439'), (b'planing_build', '\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u043a\u0430 \u0434\u043e\u043c\u0430'), (b'contacts', '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b')]),
        ),
    ]
