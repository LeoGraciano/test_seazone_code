from apps.core.abstracts import BaseModelFields
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Announcement(BaseModelFields):

    immobile = models.ForeignKey(
        "immobile.Immobile",
        verbose_name=_("Imóvel"), on_delete=models.CASCADE
    )

    platform_name = models.CharField(
        _("Nome da plataforma"), max_length=100, default=""
    )

    platform_tax = models.DecimalField(
        _("Taxa da plataforma"), max_digits=5, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = _("Anúncio")
        verbose_name_plural = _("Anúncios")
        ordering = ["created_at", "is_active"]
