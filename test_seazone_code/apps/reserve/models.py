from apps.core.abstracts import BaseModelFields
from apps.core.utils.dates import date_step, date_tomorrow
from apps.core.utils.tokens import random_code_user
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Reserve(BaseModelFields):

    code = models.CharField(
        _('Código da Reserva'), max_length=10, editable=False,
        default=random_code_user
    )

    announcement = models.ForeignKey(
        "announcement.Announcement",
        verbose_name=_("Anúncio"),
        on_delete=models.CASCADE
    )

    check_in = models.DateField(
        _("Data do Check-In"), default=date_step
    )

    check_out = models.DateField(
        _("Data do Check-Out"), default=date_tomorrow
    )

    price_total = models.DecimalField(
        _("Preço total"), max_digits=10, decimal_places=2, default=0
    )

    comment = models.TextField(
        _("Comentário"), default="", null="", blank=True
    )

    number_quests = models.PositiveSmallIntegerField(
        _("Número de hóspedes"), default=1
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")
        ordering = ["created_at", "is_active"]
