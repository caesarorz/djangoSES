# Generated by Django 2.0.2 on 2018-10-03 18:22

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('title_description', models.TextField(blank=True, null=True)),
                ('title_btn', models.CharField(default='Join', max_length=50)),
                ('title_btn_url', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('show_nav', models.BooleanField(default=True, help_text='Show Navigation Bar?')),
                ('nav_color', models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validator])),
                ('layout', models.CharField(choices=[('standard', 'Standard'), ('stacked', 'Stacked')], default='standard', max_length=20)),
                ('video_embed', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
