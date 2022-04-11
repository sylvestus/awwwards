# Generated by Django 4.0.3 on 2022-04-08 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('project_image', models.ImageField(default='', upload_to='media/')),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Design', models.IntegerField(verbose_name=range(1, 10))),
                ('Usability', models.IntegerField(verbose_name=range(1, 10))),
                ('Content', models.IntegerField(verbose_name=range(1, 10))),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePhoto', models.ImageField(default='', upload_to='media/')),
                ('bio', models.TextField()),
                ('contact', models.TextField()),
                ('projects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awardsapp.post')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='ratings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awardsapp.ratings'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]