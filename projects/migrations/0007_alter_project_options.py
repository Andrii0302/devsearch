# Generated by Django 5.1.1 on 2024-09-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]