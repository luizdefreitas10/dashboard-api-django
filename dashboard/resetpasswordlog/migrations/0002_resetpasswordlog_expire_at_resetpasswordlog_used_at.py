# Generated by Django 4.1.7 on 2023-03-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resetpasswordlog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resetpasswordlog",
            name="expire_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="resetpasswordlog",
            name="used_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
