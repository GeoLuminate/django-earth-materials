from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BgsEarthMaterialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'earth_materials'
    verbose_name = _('Earth Materials')
