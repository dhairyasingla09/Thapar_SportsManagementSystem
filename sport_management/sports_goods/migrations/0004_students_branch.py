# Generated by Django 4.1.6 on 2023-03-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sports_goods", "0003_rename_id_goods_id_alter_students_item1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="Branch",
            field=models.CharField(default=None, max_length=30),
        ),
    ]
