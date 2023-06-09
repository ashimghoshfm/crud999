# Generated by Django 4.1.7 on 2023-03-21 13:51

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
                ("eid", models.SmallIntegerField()),
                (
                    "ename",
                    models.CharField(max_length=30, verbose_name="Employee Name"),
                ),
                ("salary", models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
