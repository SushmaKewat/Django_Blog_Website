# Generated by Django 5.0 on 2023-12-26 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
