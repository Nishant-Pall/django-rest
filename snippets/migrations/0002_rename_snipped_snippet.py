# Generated by Django 4.2.1 on 2023-05-27 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snipped',
            new_name='Snippet',
        ),
    ]