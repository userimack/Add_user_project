# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trackuser', '0007_auto_20150902_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 9, 2, 11, 56, 50, 495364, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
