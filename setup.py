#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from earth_materials import __version__

REPO_URL = "https://github.com/SSJenny90/django-earth-materials"

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-earth-materials',
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    author='Sam Jennings',
    author_email='samuel.jennings@geoluminate.com.au',
    license='MIT',
    description='A Django application that provides functionality for storing earth material names (rocks, sediments, etc.) in accordance with the specifiactions set forth by the British Geological Survey.',
    url=REPO_URL,
    install_requires=[
        "Django>=3",    
        "django-treebeard==1.0.0",  
        ],
    keywords='science django geology geoscience rock classification',
    classifiers=[
        'Development Status :: 1 - Development',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)