# Django Earth Materials

Django Earth Materials is a simple app for integrating the British Geological Survey's [Earth Material Class (Rock Classification Scheme)](https://data.bgs.ac.uk/doc/EarthMaterialClass.html)[^1] into your Django app. 


[![Visualise](https://geoluminate.github.io/django-earth-materials/images/visualise.png)](https://geoluminate.github.io/django-earth-materials/visualise.html)


[^1] British Geological Survey. 2020. The BGS Rock Classification Scheme [Linked Open Data]. Keyworth, Nottingham. Available from http://data.bgs.ac.uk/ref/EarthMaterialClass

## Dependencies

The data in Django Earth Materials is stored in a Materialized Path tree structure and relies on [django-treebeard](https://github.com/django-treebeard/django-treebeard) to implement this.

## Installation

    pip install django_earth_materials

then add `earth_materials` to your installed apps like so

    INSTALLED_APPS = [
        ...
        earth_materials,
        ...
    ]

** Don't forget to run `python manage.py migrate earth_materials` to migrate the schema and load the included data fixtures!

## Usage

Django Earth Materials provides an `EarthMaterialFK`, `EarthMaterialM2M` and `EarthMaterialOneToOne` field to help you integrate the app into your project as follows:

    from earth_materials.fields import EarthMaterialFK, EarthMaterialM2M, EarthMaterialOneToOne

    class SomeModel(models.Model):
        lithology = EarthMaterialOneToOne()



Each field automatically points to the correct database table and also sub-classes fields provided by `django-treewidget` in order to utilize the `jstree` javascript widget in forms. When viewing this model in the Django Admin site, you will now be presented with a field that looks like this,

![Visualise](https://geoluminate.github.io/django-earth-materials/images/admin_widget.png)

where admin can select one or more items depending on the type of field used. The widget can be customised either by supplying the `settings` and `treeoptions` arguments to the model field or by providing customisation options project wide in `settings.py` as `TREEWIDGET_SETTINGS` and `TREEWIDGET_TREEOPTIONS`. See the readme at [`django-treewidget`](https://github.com/netzkolchose/django-treewidget) for further instructions on customisation.

## FAQ

* Why the BGS rock classification scheme and not *\*insert scheme x\**?

   The BGS rock classification scheme is a) comprehensive and well thought out; and b) readily available online making it relatively easy to import the data into a Django structure.

## Issues

The following page returns a 404 so information could not be retrieved for this particular rock type and all children that may be associated with it:

A child of Sediment and sedimentary rock could not be found at h
http://data.bgs.ac.uk/id/EarthMaterialClass/RockName/PS_PS&P 