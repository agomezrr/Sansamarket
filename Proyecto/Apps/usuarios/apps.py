from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.usuarios'

    def ready(self):
        import Apps.usuarios.signals