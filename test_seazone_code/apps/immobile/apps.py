from django.apps import AppConfig


class ImmobileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.immobile'

    def ready(self) -> None:
        import apps.immobile.signals
        return super().ready()
