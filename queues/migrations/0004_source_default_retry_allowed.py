# Generated by Django 4.1.1 on 2022-10-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queues", "0003_remove_queueitem_retries_allowed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="default_retry_allowed",
            field=models.IntegerField(default=0),
        ),
    ]