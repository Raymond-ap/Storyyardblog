# Generated by Django 3.1.3 on 2020-12-25 09:21

import django.contrib.auth.models
from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('storyyard', '0005_auto_20201225_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='BLOG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, choices=[(django.contrib.auth.models.User, django.contrib.auth.models.User)], max_length=20, null=True)),
                ('title', models.CharField(max_length=500)),
                ('banner', models.ImageField(upload_to='blog/banners')),
                ('description', djrichtextfield.models.RichTextField()),
                ('category', models.CharField(blank=True, choices=[('Romanticism', 'Romanticism'), ('Drama', 'Drama'), ('Tradegy', 'Tradegy')], max_length=30, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AUTHOR',
        ),
        migrations.DeleteModel(
            name='CATEGORY',
        ),
    ]
