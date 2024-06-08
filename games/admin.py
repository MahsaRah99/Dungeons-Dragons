from django.contrib import admin

from .models import Structure, NPC, EnemyType, Enemy, GameStructure, Game, GameCharacter


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ("name", "area", "strc_type")
    list_filter = ("strc_type",)
    search_fields = ("name",)


@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = ("name", "enm_type", "hp")


@admin.register(EnemyType)
class EnemyTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(GameStructure)
class GameStructureAdmin(admin.ModelAdmin):
    list_display = ("structure",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("name", "dungeon_master", "dc")


@admin.register(GameCharacter)
class GameCharacterAdmin(admin.ModelAdmin):
    list_display = ("player", "game", "character")
