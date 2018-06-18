from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = 'orc.utils'

    def ready(self):
        from . import checks  # noqa
