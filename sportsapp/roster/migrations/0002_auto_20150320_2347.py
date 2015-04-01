# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='hometown',
            new_name='city',
        ),
        migrations.AddField(
            model_name='player',
            name='state',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
