from rest_framework import serializers

from .models import User, Character


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")


class CharacterSerializer(serializers.ModelSerializer):
    owner = UserReadSerializer(read_only=True)

    class Meta:
        model = Character
        fields = ("owner", "name", "race", "clas", "hp", "power", "wisdom", "dexterity")

    def create(self, validated_data):
        user = self.context["request"].user
        character = Character.objects.create(owner=user, **validated_data)
        return character


class CharacterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("owner", "name", "race", "clas", "hp", "power", "wisdom", "dexterity")
        read_only_fields = ("owner", "name", "race", "clas")
