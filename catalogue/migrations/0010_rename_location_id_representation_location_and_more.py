# Generated by Django 4.1.7 on 2023-04-26 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='representation',
            old_name='location_id',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='representation',
            old_name='show_id',
            new_name='show',
        ),
    ]
