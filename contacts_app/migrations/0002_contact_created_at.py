# Generated by Django 5.0.7 on 2024-07-13 08:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
