from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "selectielijst.utils"

    def ready(self):
        from . import checks  # noqa
