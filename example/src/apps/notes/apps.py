from django.apps import AppConfig
from django.conf import settings


class NotesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.notes"

    def ready(self):
        """
        Import ORM models, set migration path and container wiring on app ready
        """
        models_module = f"{self.name}.infrastructure.orm.models"
        __import__(models_module)

        from config.container import container

        if not hasattr(settings, "MIGRATION_MODULES"):
            settings.MIGRATION_MODULES = {}
        settings.MIGRATION_MODULES[
            self.name.split(".")[-1]
        ] = f"{self.name}.infrastructure.orm.migrations"

        container.wire(modules=[f"{self.name}.interfaces.views"])
