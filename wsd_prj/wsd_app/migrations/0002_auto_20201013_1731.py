# Generated by Django 3.1.2 on 2020-10-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsd_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
