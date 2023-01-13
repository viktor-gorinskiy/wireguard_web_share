from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CertsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certs'
    verbose_name = _('certs')

    def ready(self):
        import certs.signals
