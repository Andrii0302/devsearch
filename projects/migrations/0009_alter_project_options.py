# Generated by Django 5.1.1 on 2024-09-19 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total']},
        ),
    ]
