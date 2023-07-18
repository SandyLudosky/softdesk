# Generated by Django 4.2.2 on 2023-07-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_project_contributor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contributor',
        ),
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(to='api.contributor'),
        ),
    ]
