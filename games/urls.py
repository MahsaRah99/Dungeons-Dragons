from django.urls import path

from . import views

app_name = "games"

urlpatterns = [
    path("create/", views.CreateNewGameView.as_view(), name="create_game"),
    path(
        "assign-character/",
        views.AssignCharacterView.as_view(),
        name="assign_character",
    ),
    path("show/<int:pk>/", views.GameShowView.as_view(), name="show_game"),
    path("dice/", views.DiceRolling.as_view(), name="dice_roll"),
    path(
        "character-stats/<int:pk>/",
        views.CharacterStatsView.as_view(),
        name="character_status",
    ),
    path("character-games/", views.HistoryView.as_view(), name="character_games"),
]
