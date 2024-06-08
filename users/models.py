from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .enums import CharacterRaces, CharacterClasses


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    is_verified = models.BooleanField(_("Verification status"), default=False)

    def __str__(self) -> str:
        return self.username


class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=200)
    race = models.CharField(_("Race"), max_length=2, choices=CharacterRaces.choices)
    clas = models.CharField(_("Class"), max_length=2, choices=CharacterClasses.choices)
    hp = models.FloatField(_("Hit points"))
    power = models.FloatField(_("Power"))
    wisdom = models.FloatField(_("Wisdom"))
    dexterity = models.FloatField(_("Dexterity"))

    def __str__(self) -> str:
        return self.name
