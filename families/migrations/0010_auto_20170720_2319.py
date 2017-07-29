# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-21 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_local', '0001_initial'),
        ('families', '0009_auto_20170719_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='state',
        ),
        migrations.AddField(
            model_name='family',
            name='region',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='country', chained_model_field='country', help_text='State', null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_local.Region'),
        ),
        migrations.AlterField(
            model_name='family',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='region', chained_model_field='region', on_delete=django.db.models.deletion.CASCADE, to='cities_local.City'),
        ),
        migrations.AlterField(
            model_name='family',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_local.Country'),
        ),
        migrations.AlterField(
            model_name='family',
            name='postal_code',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]