# Generated by Django 3.1.3 on 2020-12-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyyard', '0018_auto_20201226_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]