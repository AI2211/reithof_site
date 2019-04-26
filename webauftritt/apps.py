from django.apps import AppConfig


class ReithofOrganizerConfig(AppConfig):
    name = 'webauftritt'


    def ready(self):
        import webauftritt.signals