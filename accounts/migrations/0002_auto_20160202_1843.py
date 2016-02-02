# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_no',
            field=models.CharField(max_length=20, verbose_name='contact no', blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(max_length=254, verbose_name='department', blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(max_length=254, verbose_name='location', blank=True),
        ),
    ]
