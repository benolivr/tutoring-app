# Generated by Django 5.1.2 on 2024-10-17 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0017_alter_tutoringhour_hour"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutoringhour",
            name="hour",
            field=models.TimeField(
                choices=[
                    (datetime.time(7, 0), "7:00 AM"),
                    (datetime.time(8, 0), "8:00 AM"),
                    (datetime.time(9, 0), "9:00 AM"),
                    (datetime.time(10, 0), "10:00 AM"),
                    (datetime.time(11, 0), "11:00 AM"),
                    (datetime.time(12, 0), "12:00 PM"),
                    (datetime.time(13, 0), "1:00 PM"),
                    (datetime.time(14, 0), "2:00 PM"),
                    (datetime.time(15, 0), "3:00 PM"),
                    (datetime.time(16, 0), "4:00 PM"),
                    (datetime.time(17, 0), "5:00 PM"),
                    (datetime.time(18, 0), "6:00 PM"),
                    (datetime.time(19, 0), "7:00 PM"),
                    (datetime.time(20, 0), "8:00 PM"),
                ]
            ),
        ),
    ]
