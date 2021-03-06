# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rowid', models.CharField(max_length=20, null=True)),
                ('cri_comp', models.FloatField()),
                ('icl_i', models.IntegerField(null=True)),
                ('ich_i', models.IntegerField(null=True)),
                ('icm_i', models.IntegerField(null=True)),
                ('scl_s', models.IntegerField(null=True)),
                ('sch_s', models.IntegerField(null=True)),
                ('scm_s', models.IntegerField(null=True)),
                ('ca_bids', models.IntegerField(null=True)),
                ('ca_cpv', models.CharField(max_length=20, null=True)),
                ('ca_criteria_count', models.IntegerField(null=True)),
                ('ca_eufund', models.IntegerField(null=True)),
                ('ca_nuts', models.CharField(max_length=20, null=True)),
                ('ca_scntr_sc', models.IntegerField(null=True)),
                ('ca_title', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('ca_date', models.DateField(null=True)),
                ('ca_year', models.DateField(null=True)),
                ('ca_contract_value', models.FloatField(null=True)),
                ('nocft', models.IntegerField(null=True)),
                ('ca_procedure', models.CharField(max_length=50, null=True)),
                ('ca_criterion', models.CharField(max_length=50, null=True)),
                ('anb_type', models.CharField(max_length=50, null=True)),
                ('anb_sector', models.CharField(max_length=50, null=True)),
                ('anb_empl_cat', models.CharField(max_length=20, null=True)),
                ('anb_empl_cat_ordinal', models.IntegerField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CategoryCode')),
            ],
        ),
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anb_id', models.CharField(max_length=10)),
                ('anb_name', models.CharField(max_length=100)),
                ('anb_nuts', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_id', models.CharField(max_length=20)),
                ('w_name', models.CharField(max_length=200)),
                ('w_nuts', models.CharField(blank=True, max_length=100, null=True)),
                ('w_consortium', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='issuer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Issuer'),
        ),
        migrations.AddField(
            model_name='contract',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Winner'),
        ),
    ]
