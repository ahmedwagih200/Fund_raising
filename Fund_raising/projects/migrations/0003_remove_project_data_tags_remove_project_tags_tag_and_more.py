# Generated by Django 4.0.1 on 2022-02-18 20:19

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('projects', '0002_project_data_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_data',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='project_tags',
            name='tag',
        ),
        migrations.AddField(
            model_name='project_tags',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
