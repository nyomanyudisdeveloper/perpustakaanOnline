# Generated by Django 5.1.1 on 2024-09-28 07:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pinjamBuku", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transactionborrowbook",
            name="quantity",
        ),
    ]
