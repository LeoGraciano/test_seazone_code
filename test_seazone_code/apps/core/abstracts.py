from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateModelField(models.Model):
    """Classe de composição para modelos que utilizaram os
        campos created_at, updated_at
    """
    created_at = models.DateTimeField(
        _('Criado em'), auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _('Atualizado em'), auto_now=True,
    )

    class Meta:
        abstract = True


class BaseModelFields(DateModelField, models.Model):
    """Classe Abstract criada com herança do models.Models com padrão do projeto

    Fields:
        code (uuid4): primary_key
        created_at (DateTime): Data de criação
        updated_at (DateTime): Data de atualização

    Meta:
        abstract : True

    """

    id = models.UUIDField(
        primary_key=True, default=uuid4,
        editable=False,
    )

    is_active = models.BooleanField(_('Ativo'), default=True, editable=False)

    class Meta:
        abstract = True
