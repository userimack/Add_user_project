# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trackuser', '0004_remove_create_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='email',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 9, 2, 9, 33, 35, 933990, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
