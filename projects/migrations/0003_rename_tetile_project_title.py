# Generated by Django 5.1.1 on 2024-09-11 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_created_project_demo_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tetile',
            new_name='title',
        ),
    ]
