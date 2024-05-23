# Generated by Django 5.0.6 on 2024-05-21 16:09
from typing import Any
import django.db.models.deletion
import reservas.data.models.booking
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list[Any] = []

    operations = [
        migrations.CreateModel(
            name="Buyer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("booking", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Fare",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "kind",
                    models.CharField(
                        choices=[("solo-tren", "St"), ("bus-tren-bus", "Btb")], default="bus-tren-bus", max_length=255
                    ),
                ),
                ("available", models.IntegerField(default=0)),
                ("date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Pax",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("booking", models.CharField(max_length=255)),
                ("seat", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(default=reservas.data.models.booking.build_booking_code, max_length=255)),
                ("fare", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="data.fare")),
            ],
        ),
    ]
