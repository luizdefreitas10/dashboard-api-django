# Generated by Django 4.1.7 on 2023-03-15 18:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_remove_historicaluser_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicaluser",
            name="date_joined",
        ),
    ]
