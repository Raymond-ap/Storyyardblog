# Generated by Django 3.1.3 on 2020-12-27 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storyyard', '0019_auto_20201226_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2020, 12, 27, 11, 33, 29, 648620, tzinfo=utc)),
            preserve_default=False,
        ),
    ]