# Generated by Django 5.2 on 2025-04-16 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_rename_ownder_inventory_owner_alter_category_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="inventory",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventory.inventory",
            ),
            preserve_default=False,
        ),
    ]
