# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackuser', '0003_auto_20150828_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create',
            name='email',
        ),
    ]
