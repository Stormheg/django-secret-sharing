# Generated by Django 3.0.12 on 2021-03-15 09:49
import uuid

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Secret",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("value", models.BinaryField(blank=True, null=True)),
                ("erased", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        default=django.utils.timezone.now,
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="modified at"),
                ),
                ("erased_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"verbose_name": "Secret", "verbose_name_plural": "Secrets",},
        ),
    ]
