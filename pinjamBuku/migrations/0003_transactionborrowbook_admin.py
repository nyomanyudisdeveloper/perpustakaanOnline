# Generated by Django 5.1.1 on 2024-09-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pinjamBuku", "0002_remove_transactionborrowbook_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionborrowbook",
            name="admin",
            field=models.IntegerField(default=-1),
        ),
    ]
