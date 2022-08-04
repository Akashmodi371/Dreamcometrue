# Generated by Django 3.2.5 on 2021-07-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_studentblogmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='website_url',
            new_name='github_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
