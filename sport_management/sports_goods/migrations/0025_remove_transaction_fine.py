# Generated by Django 4.1.6 on 2023-04-30 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0024_transaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="fine",
        ),
    ]
