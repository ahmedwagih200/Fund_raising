# Generated by Django 2.2 on 2022-02-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_data_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_data',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='project_data',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_data',
            name='reports',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
