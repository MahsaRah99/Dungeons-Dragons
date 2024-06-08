from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game, GameStructure


@receiver(post_save, sender=Game)
def assign_structures_to_game(sender, instance, created, **kwargs):
    if created:
        selected_structures = Game.select_game_structures(instance.dc)

        with transaction.atomic():
            game_structures = [
                GameStructure(
                    structure=structure,
                    structure_enemies=GameStructure.generate_enemy_data(structure),
                    structure_npcs=GameStructure.generate_npc_data(structure),
                )
                for structure in selected_structures
            ]
            GameStructure.objects.bulk_create(game_structures)
            instance.game_structures.set(game_structures)

        instance.save()
