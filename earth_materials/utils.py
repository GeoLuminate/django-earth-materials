from multiprocessing.sharedctypes import Value
import xmltodict
import requests
from requests_cache import CachedSession
from earth_materials.models import EarthMaterial

session = CachedSession()

class BGSItem():

    def __init__(self, url, type='xml'):
        self.response = session.get(f"{url}.{type}")

        if self.response.status_code != 200:
            return 
            # raise ValueError(self.response) 

        try:
            self.xml = xmltodict.parse(self.response.text)
        except Exception as e:
            print(self.response.text)
            raise e

        self.item = self._fix_keys(self.xml)["RDF"]

        for x in ['about','inScheme','narrower','broader','type']:
            setattr(self, x, self.description.get(x))

        for x in ['term_status','label','prefLabel','definition','notation']:
            setattr(self, x, self.get(x))

    @property
    def description(self):
        return self.item['Description']

    def to_dict(self):
        return dict(
            # status = self.term_status,
            name = self.label,
            # preferred_label = self.prefLabel,
            description = self.definition,
            code = self.notation,
            url = self.about
        )

    def get(self, label):
        x = self.description.get(label)
        if x is not None:
            return x.get('#text')
        
    def children(self):
        """Returns a list of links to the children of the current item
        
        note:
        if multiple children exist, a list of object is returned;
        if a single child exist, an object only is returned
        
        """
        if isinstance(self.narrower, list):
            return [v['resource'] for v in self.narrower]
        elif isinstance(self.narrower, dict):
            return [self.narrower['resource']]
        else:
            return []

    def parent(self):
        """Returns a link to the parent of the current item"""
        return self.broader

    def _fix_keys(self, d):
        if isinstance(d, dict):
            return {k.split(':')[-1]: self._fix_keys(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [self._fix_keys(v) for v in d]
        return d

def add_children(parent, children):
    """parent is a EarthMaterial object, children are a list of the links to the child objects """
    if children:
        parent = EarthMaterial.objects.get(pk=parent.pk)

    for child_url in children:

        # creates a child BGSItem that can be queried for more children
        child = BGSItem(child_url)

        # takes relevant information from BGSItem and create a EarthMaterial instance
        # the instance is added as a child to the parent object supplied to this function call
        if child.response.status_code == 200:

            child_node = parent.add_child(**child.to_dict())

            # a recursive call to the same function to add additional descendants
            add_children(child_node, child.children())
        else:
            print(f'A child of {parent} could not be found at {child_url}')

def load():
    item = BGSItem("https://data.bgs.ac.uk/id/EarthMaterialClass/RockName/PA_RSD")



    qs = EarthMaterial.objects.filter(**item.to_dict())
    if qs.exists():
        root = qs.get(**item.to_dict())
    else:
        root = EarthMaterial.add_root(**item.to_dict())

    add_children(root, item.children())



