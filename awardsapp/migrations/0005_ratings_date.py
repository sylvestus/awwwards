# Generated by Django 4.0.3 on 2022-04-08 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0004_ratings_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
