# Generated by Django 2.1.1 on 2018-09-20 23:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=255)),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)])),
                ('ritual', models.BooleanField()),
                ('casting_time', models.BooleanField()),
                ('range', models.IntegerField()),
                ('verbal', models.BooleanField()),
                ('somatic', models.BooleanField()),
                ('material', models.CharField(max_length=255)),
                ('concentration', models.BooleanField()),
                ('duration', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]