# Generated by Django 4.1.7 on 2023-04-11 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField(auto_now_add=True)),
                ('location_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representations', to='catalogue.location')),
                ('show_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representations', to='catalogue.show')),
            ],
            options={
                'db_table': 'representations',
            },
        ),
    ]
