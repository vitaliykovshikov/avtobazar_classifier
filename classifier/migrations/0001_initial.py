# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('translit', models.SlugField(max_length=100)),
                ('sort', models.IntegerField()),
                ('status', models.IntegerField()),
                ('decomposition_data', models.CharField(max_length=4000)),
                ('ltk', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rtk', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('lvl', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='classifier.Classifier', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lng',
            fields=[
                ('lng', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Params',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value_int', models.IntegerField(null=True, blank=True)),
                ('value_timestamp', models.DateTimeField(null=True, blank=True)),
                ('value_float', models.FloatField(null=True, blank=True)),
                ('value_varchar', models.CharField(max_length=255, null=True, blank=True)),
                ('classifier', models.ForeignKey(related_name='values_classifier', to='classifier.Classifier')),
                ('lng', models.ForeignKey(blank=True, to='classifier.Lng', null=True)),
                ('params', models.ForeignKey(to='classifier.Params')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
