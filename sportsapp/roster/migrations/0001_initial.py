# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=12)),
                ('year', models.CharField(max_length=25)),
                ('hometown', models.CharField(max_length=50)),
                ('animal', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('bio', models.CharField(default=b'', max_length=700)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('coach', models.CharField(max_length=50)),
                ('description', models.CharField(default=b'', max_length=700)),
                ('players', models.ManyToManyField(to='roster.Player')),
            ],
            options={
                'ordering': ('name', 'coach'),
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
    ]
