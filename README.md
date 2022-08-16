# Django Earth Materials

Django Earth Materials is a simple app for integrating the British Geological Survey's [Earth Material Class (Rock Classification Scheme)](https://data.bgs.ac.uk/doc/EarthMaterialClass.html)[^1] into your Django app. The primary goal of this app is to help standardise the input of lithological information in Earth Science databases. 

[![Visualise](https://geoluminate.github.io/django-earth-materials/images/visualise.png)](https://geoluminate.github.io/django-earth-materials/visualise.html)

[^1] British Geological Survey. 2020. The BGS Rock Classification Scheme [Linked Open Data]. Keyworth, Nottingham. Available from http://data.bgs.ac.uk/ref/EarthMaterialClass

## Why?

Everyone who has worked with an Earth science database knows that geologists can be either very creative or incredibly specific when they assign a name to a particular sample they are working with (e.g. hyper-crystallised, megalodon-tooth-bearing niche schist). While this sort of freedom is useful in covering geological edge-cases, from a database perspective it makes it very difficult to aggregate, process, analyse and share data. 

Standards such as the BGS Earth Material Class have been developed to address this issue and geologists are kindly asked to adhere to the scheme when classifying their samples. Unfortunately, there are still some issues that lead to poor reporting:

1) Nothing is done to enforce usage of any particular classification scheme
2) In order to make use of a classification scheme, the geologist/researcher must actively look up the closest match for each sample
3) When an attempt is made to do this, simple things like spelling or formatting errors can lead to the same rock types being listed multiple times

Django Earth Materials tries to address these issues by **enforcing** use of the BGS classification scheme through a simple tree-based select widget. In this way, a single scheme is in use across all databases that make use of this app, users don't have to go looking for the correct classification on external sites, and spelling/formatting errors are eliminated.

## Installation

First install the application with pip using

    pip install django_earth_materials

then add `earth_materials` to your installed apps like so

    INSTALLED_APPS = [
        ...
        earth_materials,
        ...
    ]

Finally, add the earth_materials urls to your project urls

    urlpatterns = [
        ...
        path('earth_materials', include('earth_materials.urls')),
        ...
    ]

> **_NOTE:_**  Don't forget to run `python manage.py migrate earth_materials` to migrate the schema and load the included data fixtures!


## Usage

Django Earth Materials provides an `EarthMaterialFK`, `EarthMaterialM2M` and `EarthMaterialOneToOne` field to help you integrate the app into your project as follows:

    from earth_materials.fields import EarthMaterialFK, EarthMaterialM2M, EarthMaterialOneToOne

    class SomeModel(models.Model):
        lithology = EarthMaterialOneToOne()

Each field automatically points to the EarthMaterial model and also sub-classes fields provided by `django-treewidget` in order to utilize the `jstree` javascript widget in forms. When viewing this model in the Django Admin site, you will now be presented with a field like this,

![Visualise](https://geoluminate.github.io/django-earth-materials/images/admin_widget.PNG)

where admin can select one or more items depending on the type of field used. 

> **_NOTE:_**  The above image is taken from an admin site that utilizes the [Djang Grappelli](https://grappelliproject.com) admin interface. If you don't use Grappelli then your field may look slightly different.


## Settings

Django Earth Materials includes two settings, `EARTH_MATERIALS_INCLUDE` and `EARTH_MATERIALS_EXCLUDE`, that can be declared in your `settings.py` file to control what tree nodes are available in the form widget. These are useful if your project is dedicated to a specific rock group. For example, 

    EARTH_MATERIALS_INCLUDE = [
        'Igneous rock and sediment',
        'Metamorphic rock',
        ]

will restrict the widget to only igneous and metamorphic rock types. Alternatively,

    EARTH_MATERIALS_EXCLUDE = [
        'Superficial deposit (natural and/or artificial)'
        ]
        
will exclude artificial materials from the widget.

> **_NOTE:_** If both `EARTH_MATERIALS_INCLUDE` and `EARTH_MATERIALS_EXCLUDE` are found in `settings.py`, only `EARTH_MATERIALS_INCLUDE` will be used.

## Customisation

The widget can be customised either by supplying the `settings` and `treeoptions` arguments to the model field or by providing customisation options project wide in `settings.py` as `TREEWIDGET_SETTINGS` and `TREEWIDGET_TREEOPTIONS`. See the readme at [`django-treewidget`](https://github.com/netzkolchose/django-treewidget) for further instructions on customisation.

The following settings are recommended here but not required:

> **_NOTE:_**  To use, place these in your `settings.py` file.

    TREEWIDGET_SETTINGS = {
                'search':True, # adds a search bar to the widget that filters tree nodes
                }
                
    TREEWIDGET_TREEOPTIONS = {
        "core" : {
            "themes" : {
                "icons": False, # removes the folder icon next to each item
            },
        },
        "plugins" : [ "checkbox" ] # adds checkboxes next to each item
    }


## FAQ

* Why the BGS rock classification scheme and not *\*insert scheme x\**?

   The BGS rock classification scheme is a) comprehensive and well thought out; and b) readily available online making it relatively easy to import the data into a Django structure.

## Issues & Inconsistencies

The following pages returned a 404 during the data gathering stage so no information could be retrieved from it or any associated children:

* A child of Sediment and sedimentary rock could not be found at http://data.bgs.ac.uk/id/EarthMaterialClass/RockName/PS_PS&P 
