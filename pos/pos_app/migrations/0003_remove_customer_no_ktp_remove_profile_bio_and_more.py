# Generated by Django 5.0.6 on 2024-06-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pos_app", "0002_carcategory_car_customer_payment_inforent_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="no_ktp",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="bio",
        ),
        migrations.AddField(
            model_name="profile",
            name="no_ktp",
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_customer",
            field=models.BooleanField(default=False),
        ),
    ]
