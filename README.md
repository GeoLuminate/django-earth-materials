# Django Earth Materials

Django Earth Materials is a Django app for integrating the British Geological Survey's [Earth Material Class (Rock Classification Scheme)](https://data.bgs.ac.uk/doc/EarthMaterialClass.html)<sup>1</sup> into your Django app. 


[![Visualise](https://geoluminate.github.io/django-earth-materials/images/visualise.png)](https://geoluminate.github.io/django-earth-materials/visualise.html)


<sup>1</sup> British Geological Survey. 2020. The BGS Rock Classification Scheme [Linked Open Data]. Keyworth, Nottingham. Available from http://data.bgs.ac.uk/ref/EarthMaterialClass

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

## Basic Usage

Django Earth Materials is a very basic app that simply creates a new database table and preloads data sourced from the BGS online data service. As such, you can link to it in all the usual Django ways for related fields such as OneToOne, ForeignKey or ManyToMany.


## FAQ

Why the BGS rock classification scheme and not *\*insert scheme x\**?



## Issues

The following page returns a 404 so information could not be retrieved for this particular rock type and all children that may be associated with it:

A child of Sediment and sedimentary rock could not be found at h
http://data.bgs.ac.uk/id/EarthMaterialClass/RockName/PS_PS&P 