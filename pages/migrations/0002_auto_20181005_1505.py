# Generated by Django 2.0.2 on 2018-10-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='page',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
