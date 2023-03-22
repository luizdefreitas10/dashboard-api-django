# Generated by Django 4.1.7 on 2023-03-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_remove_historicaluser_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaluser",
            name="history_type",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Changed", "Changed"),
                    ("Deleted", "Deleted"),
                ],
                max_length=100,
            ),
        ),
    ]
