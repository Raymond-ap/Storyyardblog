# Generated by Django 3.1.3 on 2020-12-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyyard', '0003_auto_20201225_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.CharField(choices=[('Gorge', 'Gorge')], default=0, max_length=20),
        ),
    ]