import random
from rest_framework import serializers

from users.models import User, Character

from .models import Game, GameCharacter, GameStructure, Structure


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ("name", "area", "strc_type", "npc_count", "enemy_count", "dc")


class GameStructureSerializer(serializers.ModelSerializer):
    structure = StructureSerializer(read_only=True)

    class Meta:
        model = GameStructure
        fields = ("structure", "structure_enemies", "structure_npcs")


class GameSerializer(serializers.ModelSerializer):
    dungeon_master = serializers.ReadOnlyField(source="dungeon_master.username")
    players = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(), many=True
    )
    game_structures = GameStructureSerializer(read_only=True, many=True)
    characters = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "name",
            "dungeon_master",
            "players",
            "dc",
            "start_at",
            "end_at",
            "characters",
            "game_structures",
        )
        read_only_fields = ("dungeon_master", "game_structures")

    def create(self, validated_data):
        players_data = validated_data.pop("players")
        game = Game.objects.create(
            dungeon_master=self.context["request"].user, **validated_data
        )
        for player in players_data:
            GameCharacter.objects.create(player=player, game=game)
        return game

    def get_characters(self, obj: Game):
        qs = GameCharacter.objects.filter(game=obj)
        return qs.values_list("character__name", flat=True)


class GameShortSerializer(serializers.ModelSerializer):
    dungeon_master = serializers.ReadOnlyField(source="dungeon_master.username")

    class Meta:
        model = Game
        fields = (
            "id",
            "name",
            "dungeon_master",
            "dc",
            "start_at",
            "end_at",
        )
        read_only_fields = ("dungeon_master",)


class AssignCharacterSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all())

    class Meta:
        model = GameCharacter
        fields = ("character",)

    def validate_character(self, value):
        if value.owner != self.context["request"].user:
            raise serializers.ValidationError(
                "You can only assign your own characters."
            )
        return value
