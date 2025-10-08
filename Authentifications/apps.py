from django.apps import AppConfig


class AuthentificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Authentifications'

    def ready(self):
        import Authentifications.signals