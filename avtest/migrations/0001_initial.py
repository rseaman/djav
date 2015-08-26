# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alienvaultid', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=15)),
                ('timestamp', models.CharField(max_length=10)),
                ('endpoint', models.CharField(max_length=128)),
            ],
        ),
    ]
