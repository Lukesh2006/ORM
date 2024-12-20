# Generated by Django 5.1.3 on 2024-11-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("eid", models.CharField(help_text="Employee.ID", max_length=20)),
                ("name", models.CharField(max_length=100)),
                ("salary", models.ImageField(upload_to="")),
                ("age", models.ImageField(upload_to="")),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
