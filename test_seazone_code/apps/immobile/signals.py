
from django.utils import timezone


from apps.immobile.models import Immobile

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from django.db.models import Exists, OuterRef, Q, Count, F, Max, Sum, Q


@receiver(pre_save, sender=Immobile)
def immobile_is_active(sender, instance, **kwargs):
    if instance.is_active:
        instance.active_at = timezone.now()
