# Generated by Django 4.1 on 2022-08-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0011_alter_letter_color_alter_letter_font_family_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="letter",
            name="color",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="letter",
            name="font_family",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="letter",
            name="font_size",
            field=models.CharField(max_length=30, null=True),
        ),
    ]