# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0002_auto_20150320_2347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('last', 'first')},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='first_name',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='last_name',
            new_name='last',
        ),
    ]
