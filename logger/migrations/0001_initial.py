# Generated by Django 4.1.5 on 2023-01-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="i18nLog",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("key", models.CharField(max_length=255)),
                ("hits", models.IntegerField(default=0)),
                ("misses", models.IntegerField(default=0)),
                (
                    "locale",
                    models.CharField(
                        choices=[("en", "English"), ("es", "Spanish")], max_length=2
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "i18n Log",
                "verbose_name_plural": "i18n Logs",
                "db_table": "i18n_log",
            },
        ),
    ]
