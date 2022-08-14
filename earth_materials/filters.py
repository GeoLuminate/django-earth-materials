from django.contrib import admin
from django.utils.translation import gettext as _

class TreeNodeDepthFilter(admin.SimpleListFilter):

    title = _('Material')
    parameter_name = 'material'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request).filter(depth__lte=model_admin.node_filter_depth)
        return ((v.id, v) for v in qs)

    def queryset(self, request, qs):
        filtered = qs.filter(id=self.value())
        if filtered.exists():
            return filtered.get(id=self.value()).get_descendants()
        else:
            return qs
    