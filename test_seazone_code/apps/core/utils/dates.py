from datetime import datetime, timedelta
from django.utils import timezone


def date_step(step=0):
    _dt = timezone.now() + timedelta(days=step)
    return _dt.date()


def date_tomorrow():
    return date_step(step=1)
