# Generated by Django 4.1.7 on 2023-03-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accesslog", "0002_remove_useraccesslog_ip_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccesslog",
            name="ip_address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
