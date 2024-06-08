from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import CharacterStatusSerializer

from .models import Game, GameCharacter
from .permissions import CharacterStatusPermission, GamePlayers
from .serializers import GameSerializer, GameShortSerializer, AssignCharacterSerializer
from .utils import roll_dices


class CreateNewGameView(generics.CreateAPIView):
    queryset = Game.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer


class AssignCharacterView(generics.UpdateAPIView):
    queryset = GameCharacter.objects.all()
    serializer_class = AssignCharacterSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.request.data.get("game_id")
        user = self.request.user
        try:
            game_character = GameCharacter.objects.get(game_id=game_id, player=user)
        except GameCharacter.DoesNotExist:
            raise PermissionDenied("You are not a player in this game.")
        return game_character


class GameShowView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [GamePlayers]


class DiceRolling(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dice_data = request.data
        result = roll_dices(dice_data)
        return Response(result)


class CharacterStatsView(generics.RetrieveUpdateAPIView):
    queryset = GameCharacter.objects.all()
    serializer_class = CharacterStatusSerializer
    permission_classes = [CharacterStatusPermission]

    def get_object(self):
        character_game = super().get_object()
        character = character_game.character
        return character


class HistoryView(generics.ListAPIView):
    serializer_class = GameShortSerializer
    # permission_classes = [CharacterOwner]

    def get_queryset(self):
        character_id = self.request.query_params.get("character_id")
        qs = GameCharacter.objects.filter(character_id=character_id)
        game_ids = qs.values_list("game", flat=True).distinct()
        return Game.objects.filter(id__in=game_ids)
