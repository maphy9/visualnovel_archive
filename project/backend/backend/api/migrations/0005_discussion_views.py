# Generated by Django 5.1.6 on 2025-02-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_visualnovel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
