# Generated by Django 3.1.3 on 2020-12-25 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storyyard', '0011_blog_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
