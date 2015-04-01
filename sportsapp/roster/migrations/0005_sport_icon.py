# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0004_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='icon',
            field=models.CharField(default=b'', max_length=70),
            preserve_default=True,
        ),
    ]
