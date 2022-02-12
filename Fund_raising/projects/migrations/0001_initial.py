# Generated by Django 4.0.1 on 2022-02-12 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=800)),
                ('target', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('reports', models.IntegerField(default=0)),
                ('current_money', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
