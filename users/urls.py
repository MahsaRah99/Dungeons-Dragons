from django.urls import path

from rest_framework import routers

from . import views

app_name = "users"

router = routers.SimpleRouter()
router.register("character", views.CharacterViewSet)
urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="user_register"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("my-characters/", views.MyCharactersListView.as_view(), name="my_characters"),
] + router.urls
