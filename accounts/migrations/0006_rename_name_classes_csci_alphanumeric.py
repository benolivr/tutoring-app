# Generated by Django 5.1.2 on 2024-10-14 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_customuser_tutor_email_customuser_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="classes",
            old_name="name",
            new_name="cSCI_Alphanumeric",
        ),
    ]
