from django.apps import AppConfig


class ReithofOrganizerConfig(AppConfig):
    name = 'reithof_organizer'


    def ready(self):
        import reithof_organizer.signals