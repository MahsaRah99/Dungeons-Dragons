from django.utils.translation import gettext_lazy as _
from django.db import models


class StructureTypes(models.TextChoices):
    PLAIN = "PL", _("Plain")
    MOUNTAINS = "MT", _("Mountains")
    ROAD = "RD", _("Road")
    DUNGEON = "DG", _("Dungeon")
