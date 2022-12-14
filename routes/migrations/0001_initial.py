# Generated by Django 4.1.1 on 2022-09-13 13:34

from django.db import migrations, models
import routes.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Route",
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
                (
                    "name",
                    models.CharField(
                        help_text="The name of the route between points",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="You can include tech of the route. For example SMS route or EGPAF WAN route",
                        null=True,
                    ),
                ),
                (
                    "weight",
                    models.IntegerField(
                        default=1,
                        help_text="A route should have a unique weighting",
                        unique=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Up", "Up"),
                            ("Down", "Down"),
                            ("Unknown", "Unknown"),
                        ],
                        default="Unknown",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
