# Generated by Django 2.2 on 2022-02-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20220214_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
