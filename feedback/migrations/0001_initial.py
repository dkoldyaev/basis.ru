# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField(default=True, help_text='\u0415\u0441\u043b\u0438 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043e, \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439. \u0415\u0441\u043b\u0438 \u0441\u043d\u044f\u0442\u043e \u2014 \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445', verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u0441\u0430\u0439\u0442\u0435')),
                ('_created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('_updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('_comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('_active', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('_deleted', models.BooleanField(default=False, verbose_name='\u0423\u0434\u0430\u043b\u0435\u043d\u043e')),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='Email', blank=True)),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('message', models.TextField()),
                ('page', models.CharField(max_length=255, null=True, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0441\u0430\u0439\u0442\u0430', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField(default=True, help_text='\u0415\u0441\u043b\u0438 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043e, \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439. \u0415\u0441\u043b\u0438 \u0441\u043d\u044f\u0442\u043e \u2014 \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445', verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u0441\u0430\u0439\u0442\u0435')),
                ('_created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('_updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('_comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('_active', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('_deleted', models.BooleanField(default=False, verbose_name='\u0423\u0434\u0430\u043b\u0435\u043d\u043e')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
