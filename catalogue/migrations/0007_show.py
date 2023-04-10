# Generated by Django 4.1.7 on 2023-04-10 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255, null=True)),
                ('posterUrl', models.CharField(max_length=255, null=True)),
                ('bookable', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shows', to='catalogue.location')),
            ],
            options={
                'db_table': 'shows',
            },
        ),
    ]
