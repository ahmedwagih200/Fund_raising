# Generated by Django 2.2 on 2022-02-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20220216_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='remain',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
