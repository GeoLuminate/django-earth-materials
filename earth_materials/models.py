from weakref import proxy
from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.translation import gettext as _

class EarthMaterial(MP_Node):
    name = models.CharField(_('Name'),
        help_text=_('Name of the earth material'),
        max_length=255)
    description = models.TextField(_('Description'),
        help_text=_('Description of the material'),
        max_length=255, 
        blank=True, null=True)
    code = models.CharField(_('Code'), 
        help_text=_('Identifier code'),
        max_length=16, 
        blank=True, null=True)
    url = models.URLField(_('About'),
        help_text=_('URL to the page describing the field on the BGS website'),
    )

    node_order_by = ['label']

    class Meta:
        verbose_name = _('Earth Material')
        verbose_name_plural = _('Earth Materials')

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def autocomplete_search_fields():
        # For Django Grappelli related lookups
        return ("label__icontains", "notation__icontains",)
