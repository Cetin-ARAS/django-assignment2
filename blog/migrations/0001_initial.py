# Generated by Django 4.1.4 on 2023-01-01 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.IntegerField(blank=True, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.TextField()),
                ("content", models.CharField(max_length=30)),
                ("cotegory_id", models.IntegerField(blank=True, null=True)),
                ("status", models.BooleanField(default=False)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="student_api.category",
                    ),
                ),
            ],
        ),
    ]
