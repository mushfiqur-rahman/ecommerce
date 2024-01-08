from django.apps import AppConfig


class StoreCustomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self) -> None:
        import main.signals.handlers
