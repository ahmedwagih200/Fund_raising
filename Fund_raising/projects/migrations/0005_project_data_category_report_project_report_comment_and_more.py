# Generated by Django 4.0.1 on 2022-02-12 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='category',
            field=models.ForeignKey(default='non categorized', on_delete=django.db.models.deletion.CASCADE, to='projects.category'),
        ),
        migrations.CreateModel(
            name='Report_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reported', models.BooleanField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_project', to='projects.project_data')),
            ],
        ),
        migrations.CreateModel(
            name='Report_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_id', to='projects.project_comments')),
            ],
        ),
        migrations.CreateModel(
            name='Rate_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_project', to='projects.project_data')),
            ],
        ),
        migrations.CreateModel(
            name='project_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project_data')),
            ],
        ),
        migrations.CreateModel(
            name='Donate_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donated_project', to='projects.project_data')),
            ],
        ),
    ]
