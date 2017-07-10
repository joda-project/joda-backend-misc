# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joda_misc', '0002_default_misc_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscdocument',
            options={'verbose_name': 'miscellaneous document', 'verbose_name_plural': 'miscellaneous documents'},
        ),
        migrations.AlterModelOptions(
            name='misctype',
            options={'verbose_name': 'miscellaneous document type', 'verbose_name_plural': 'miscellaneous document types'},
        ),
        migrations.AlterField(
            model_name='miscdocument',
            name='misc_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='joda_misc.MiscType', verbose_name='miscellaneous document type'),
        ),
        migrations.AlterField(
            model_name='misctype',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name'),
        ),
    ]