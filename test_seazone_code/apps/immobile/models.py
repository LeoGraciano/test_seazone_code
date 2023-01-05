from apps.core.abstracts import BaseModelFields
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.utils.tokens import random_key


class immobile(BaseModelFields):

    code = models.CharField(
        _('Código do imóvel'), max_length=8, unique=True,
        default=random_key
    )

    limit_guests = models.PositiveSmallIntegerField(
        _("Limite de hóspedes"), default=1
    )

    qty_bathrooms = models.PositiveSmallIntegerField(
        _("Quantidade de banheiros"), default=0
    )

    accept_pet = models.BooleanField(
        _("Aceita Animais"), default=False
    )

    cleaning_value = models.DecimalField(
        _("Valor da limpeza"), max_digits=10, decimal_places=2, default=0
    )

    def __str__(self):
        active = "Ativo"
        if not self.is_active:
            active = "Desativado"

        return f"{self.code} - {active}"

    class Meta:
        verbose_name = _("Imóvel")
        verbose_name_plural = _("Imóveis")
        ordering = ['created_at', 'is_active']
