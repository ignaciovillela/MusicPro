# Generated by Django 4.2.1 on 2023-05-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0005_order_tom_bank_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="usd_value",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
