# Generated by Django 2.0.5 on 2018-05-03 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blue', '0007_auto_20180503_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 3, 13, 10, 31, 964258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='viewers',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 3, 13, 10, 31, 964770, tzinfo=utc)),
        ),
    ]
