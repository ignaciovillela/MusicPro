# Generated by Django 4.2.1 on 2023-05-07 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20230505_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='currency_exchange',
        ),
    ]
