from rest_framework.permissions import SAFE_METHODS

from users.permissions import PrimaryPermission


class CharacterStatusPermission(PrimaryPermission):
    def has_object_permission(self, request, view, obj):
        game = obj.game
        if request.method in SAFE_METHODS:
            return request.user in game.players.all()
        return game.dungeon_master == request.user


class GamePlayers(PrimaryPermission):
    message = "permission denied"

    def has_object_permission(self, request, view, obj):
        return request.user in obj.players.all() or request.user == obj.dungeon_master
