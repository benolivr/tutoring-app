# Generated by Django 5.1.2 on 2024-10-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0013_alter_tutoringhour_hour"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutoringhour",
            name="hour",
            field=models.TimeField(
                choices=[
                    ("7:00:00", "7:00:00"),
                    ("8:00:00", "8:00:00"),
                    ("9:00:00", "9:00:00"),
                    ("10:00:00", "10:00:00"),
                    ("11:00:00", "11:00:00"),
                    ("12:00:00", "12:00:00"),
                    ("13:00:00", "13:00:00"),
                    ("14:00:00", "14:00:00"),
                    ("15:00:00", "15:00:00"),
                    ("16:00:00", "16:00:00"),
                    ("17:00:00", "17:00:00"),
                    ("18:00:00", "18:00:00"),
                    ("19:00:00", "19:00:00"),
                    ("20:00:00", "20:00:00"),
                ]
            ),
        ),
    ]
