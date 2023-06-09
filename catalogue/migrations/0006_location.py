# Generated by Django 4.1.7 on 2023-04-10 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('designation', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locations', to='catalogue.locality')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
    ]
