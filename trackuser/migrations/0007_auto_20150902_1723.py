# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackuser', '0006_remove_create_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='username',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
