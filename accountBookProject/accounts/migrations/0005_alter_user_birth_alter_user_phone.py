# Generated by Django 4.2.1 on 2023-08-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(default="", max_length=100),
        ),
    ]
