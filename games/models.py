from random import randint
import random
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .enums import StructureTypes


class Structure(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    area = models.FloatField(_("Area"))
    strc_type = models.CharField(
        _("Type"), max_length=2, choices=StructureTypes.choices
    )

    @property
    def enemy_count(self):
        match self.strc_type:
            case "PL" | "MT":
                return randint(1, 3)
            case "RD":
                return int(self.area // 100)
            case "DG":
                return int(self.area // 50)

    @property
    def npc_count(self):
        match self.strc_type:
            case "PL" | "MT":
                return randint(0, 1)
            case "RD":
                return int(self.area // 300)
            case "DG":
                return 0

    @property
    def dc(self):
        """(Enemy_count * 1 + NPC_count * -1) / strcuture_surface * 100"""
        return ((self.enemy_count - self.npc_count) / (self.area)) * 100


class GameStructure(models.Model):
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    structure_enemies = models.JSONField(_("Enemies"))
    structure_npcs = models.JSONField(_("NPCs"))

    @staticmethod
    def generate_npc_data(structure):
        npcs = list(NPC.objects.all())
        npc_data = {}
        for _ in range(structure.npc_count):
            npc = random.choice(npcs)
            if npc.id in npc_data:
                npc_data[npc.id] += 1
            else:
                npc_data[npc.id] = 1
        return npc_data

    @staticmethod
    def generate_enemy_data(structure):
        enemies = list(Enemy.objects.all())
        enemy_data = {}
        for _ in range(structure.enemy_count):
            enemy = random.choice(enemies)
            if enemy.id in enemy_data:
                enemy_data[enemy.id] += 1
            else:
                enemy_data[enemy.id] = 1
        return enemy_data


class Game(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    dungeon_master = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="directed_games",
        on_delete=models.PROTECT,
    )
    players = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="GameCharacter",
        related_name="played_games",
    )
    game_structures = models.ManyToManyField("games.GameStructure")
    dc = models.FloatField(_("Difficulty Class"))
    start_at = models.DateTimeField(_("Start"))
    end_at = models.DateTimeField(_("End"))

    @staticmethod
    def select_game_structures(game_dc):
        structures = list(Structure.objects.all())
        random.shuffle(structures)
        selected_structures = []
        total_dc = 0

        for structure in structures:
            if total_dc + structure.dc <= game_dc:
                selected_structures.append(structure)
                total_dc += structure.dc
            if total_dc == game_dc:
                break
        return selected_structures

    def __str__(self) -> str:
        return self.name


class GameCharacter(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    character = models.ForeignKey(
        "users.Character", null=True, on_delete=models.SET_NULL
    )

    class Meta:
        unique_together = ("player", "game")

    def __str__(self) -> str:
        return f"{self.character}-{self.game}"


class NPC(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    def __str__(self) -> str:
        return self.name


class EnemyType(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    def __str__(self) -> str:
        return self.name


class Enemy(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    enm_type = models.ForeignKey(EnemyType, on_delete=models.CASCADE)
    description = models.TextField(_("Description"))
    hp = models.FloatField(_("Hit points"))
    min_power = models.FloatField(_("Minimum Power"))
    max_power = models.FloatField(_("Maximum Power"))

    def __str__(self) -> str:
        return self.name

    @property
    def power_range(self):
        return (self.min_power, self.max_power)

    @property
    def dc(self):
        """HP * 0.2 + 0.1 * (maximum_power + minimum_power) / 2"""
        return self.hp * 0.2 + 0.1 * (self.max_power + self.min_power) / 2
