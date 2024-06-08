# Generated by Django 5.0.6 on 2024-06-08 12:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("games", "0001_initial"),
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="dungeon_master",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="directed_games",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="gamecharacter",
            name="character",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.character",
            ),
        ),
        migrations.AddField(
            model_name="gamecharacter",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="games.game"
            ),
        ),
        migrations.AddField(
            model_name="gamecharacter",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="players",
            field=models.ManyToManyField(
                related_name="played_games",
                through="games.GameCharacter",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="game_structures",
            field=models.ManyToManyField(to="games.gamestructure"),
        ),
        migrations.AddField(
            model_name="gamestructure",
            name="structure",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="games.structure"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="gamecharacter",
            unique_together={("player", "game")},
        ),
    ]
