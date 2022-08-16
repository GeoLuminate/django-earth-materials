from django.db.models import Q, F
from django.db.models.functions import Substr

ParentPath = Substr('path', 1, (F('depth') - 1) * 4 )

def include_descendants(queryset=None):
        descendants = Q()
        nodes = queryset.values('path', 'depth')
        for node in nodes:
            descendants |= Q(path__startswith=node['path'], depth__gt=node['depth'])
        return queryset.model.objects.filter(Q(id__in=queryset.values_list('id')) | descendants)

def include_ancestors(queryset=None):
        queryset = queryset.annotate(root=Substr('path', 1, queryset.model.steplen))
        nodes = list(set(queryset.values_list('root', 'depth')))

        ancestors = Q()
        for node in nodes:
            ancestors |= Q(path__startswith=node[0], depth__lt=node[1])
        return queryset.model.objects.filter(Q(id__in=queryset.values_list('id')) | ancestors)
