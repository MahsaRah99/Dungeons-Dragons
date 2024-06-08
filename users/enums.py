from django.utils.translation import gettext_lazy as _
from django.db import models


class CharacterRaces(models.TextChoices):
    DRAGONBORN = "DB", _("Dragon Born")
    DWARF = "DW", _("Dwarf")
    ELF = "EL", _("Elf")
    GNOME = "GN", _("Gnome")
    HALF_ELF = "HE", _("Half Elf")
    HALFLING = "HL", _("Halfling")
    HALF_ORC = "HO", _("Half Orc")
    HUMAN = "HU", _("Human")
    TIEFLING = "TL", _("Tiefling")


class CharacterClasses(models.TextChoices):
    BARBARIAN = "BR", _("Barbarian")
    BARD = "BA", _("Bard")
    CLERIC = "CL", _("Cleric")
    DRUID = "DR", _("Druid")
    FIGHTER = "FI", _("Fighter")
    MONK = "MO", _("Monk")
    PALADIN = "PA", _("Paladin")
    RANGER = "RA", _("Ranger")
    ROGUE = "RO", _("Rogue")
    SORCERER = "SO", _("Sorcerer")
    WARLOCK = "WL", _("Warlock")
    WIZARD = "WI", _("Wizard")
