# Generated by Django 2.0.5 on 2018-05-07 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_description',
            new_name='event_description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_title',
            new_name='event_title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='city',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_type',
        ),
    ]
