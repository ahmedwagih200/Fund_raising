# Generated by Django 4.0.2 on 2022-02-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='photo',
        ),
    ]
