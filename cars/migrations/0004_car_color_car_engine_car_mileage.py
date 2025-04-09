# Generated by Django 5.2 on 2025-04-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0003_car_photo_car_plate"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="car",
            name="engine",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="car",
            name="mileage",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
