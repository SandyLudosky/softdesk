# Generated by Django 4.2.2 on 2023-07-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_project_contributor_project_contributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(blank=True, default=[], to='api.contributor'),
        ),
    ]
