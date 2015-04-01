# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0005_sport_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
