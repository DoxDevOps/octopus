# Generated by Django 4.1.1 on 2022-09-13 15:06

from django.db import migrations, models
import django.db.models.deletion
import routes.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    routes.models.UuidField(
                        default=uuid.uuid4, max_length=128, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "default_destination",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("default_retry_count_allowed", models.IntegerField(default=3)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="QueueItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    routes.models.UuidField(
                        default=uuid.uuid4, max_length=128, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("destination", models.CharField(max_length=255, null=True)),
                ("payload", models.TextField(blank=True, null=True)),
                ("encrypt_before_sending", models.BooleanField(default=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Queued", "Queued"),
                            ("Sent", "Sent"),
                            ("Failed", "Failed"),
                        ],
                        default="Queued",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("retries_allowed", models.IntegerField(default=3)),
                ("retry_attempt_count", models.IntegerField(default=0)),
                (
                    "source",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="queues.source",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
