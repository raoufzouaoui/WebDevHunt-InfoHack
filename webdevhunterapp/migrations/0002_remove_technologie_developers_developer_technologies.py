# Generated by Django 4.0.2 on 2022-02-27 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdevhunterapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technologie',
            name='developers',
        ),
        migrations.AddField(
            model_name='developer',
            name='technologies',
            field=models.ManyToManyField(to='webdevhunterapp.Technologie'),
        ),
    ]
