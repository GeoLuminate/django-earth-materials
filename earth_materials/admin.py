from django.contrib import admin
from .models import EarthMaterial
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from django.core.paginator import Paginator
from .filters import TreeNodeDepthFilter

# Register your models here.
class EarthMaterialTreeAdmin(TreeAdmin):
    form = movenodeform_factory(EarthMaterial)
    node_filter_depth = 2
    search_fields = [
        'name','code',
    ]

class EarthMaterialAdmin(admin.ModelAdmin):
    form = movenodeform_factory(EarthMaterial)
    list_display = ['name','code','description']
    # list_filter = ['status','depth']
    search_fields = [
        'name','code', 
    ]


admin.site.register(EarthMaterial, EarthMaterialTreeAdmin)
# admin.site.register(EarthMaterialProxy, EarthMaterialAdmin)