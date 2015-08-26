# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alienvaultid', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=15)),
                ('timestamp', models.CharField(max_length=10)),
                ('endpoint', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to='avtest.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Visits',
        ),
    ]
