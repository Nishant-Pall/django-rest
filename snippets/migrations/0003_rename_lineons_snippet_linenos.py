# Generated by Django 4.2.1 on 2023-05-27 16:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("snippets", "0002_rename_snipped_snippet"),
    ]

    operations = [
        migrations.RenameField(
            model_name="snippet",
            old_name="lineons",
            new_name="linenos",
        ),
    ]
