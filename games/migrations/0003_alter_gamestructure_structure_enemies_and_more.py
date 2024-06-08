# Generated by Django 5.0.6 on 2024-06-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gamestructure",
            name="structure_enemies",
            field=models.JSONField(null=True, verbose_name="Enemies"),
        ),
        migrations.AlterField(
            model_name="gamestructure",
            name="structure_npcs",
            field=models.JSONField(null=True, verbose_name="NPCs"),
        ),
    ]