# Generated by Django 4.0.6 on 2022-07-13 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userprofile_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReportUser',
            new_name='Report',
        ),
    ]
