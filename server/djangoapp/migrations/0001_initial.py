# Generated by Django 5.1.3 on 2024-11-12 02:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id',
                 models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[
                    ('SEDAN', 'Sedan'), ('SUV', 'SUV'),
                    ('WAGON', 'Wagon')], default='SUV',
                    max_length=15)),
                ('year', models.IntegerField(default=2024,
                 validators=[
                        django.core.validators.MaxValueValidator(2024),
                        django.core.validators.MinValueValidator(2015)])),
                ('car_make', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='djangoapp.carmake')),
            ],
        ),
    ]
