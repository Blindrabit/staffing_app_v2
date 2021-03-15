from django.apps import AppConfig


class ShiftsConfig(AppConfig):
    name = 'shifts'

    def ready(self):
        import shifts.signals
