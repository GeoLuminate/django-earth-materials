from treewidget.fields import TreeOneToOneField, TreeForeignKey, TreeManyToManyField

class EarthMaterialFK(TreeForeignKey):
    def __init__(self, *args, **kwargs):
        kwargs['to'] = "earth_materials.EarthMaterial"
        super().__init__(*args, **kwargs)


class EarthMaterialOneToOne(TreeOneToOneField):
    def __init__(self, *args, **kwargs):
        kwargs['to'] = "earth_materials.EarthMaterial"
        super().__init__(*args, **kwargs)

class EarthMaterialM2M(TreeManyToManyField):
    def __init__(self, *args, **kwargs):
        kwargs['to'] = "earth_materials.EarthMaterial"
        super().__init__(*args, **kwargs)
