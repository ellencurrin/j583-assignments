# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0003_auto_20150323_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.CharField(default=b'', max_length=700)),
                ('teams', models.ManyToManyField(to='roster.Team')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Sports',
            },
            bases=(models.Model,),
        ),
    ]
