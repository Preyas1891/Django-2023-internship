# Generated by Django 4.1.7 on 2023-03-11 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student3',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student3',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
