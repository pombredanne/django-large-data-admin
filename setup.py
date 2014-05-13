#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-large-data-admin",
    version = "1.14.0",
    url = 'https://github.com/sikaondrej/django-large-data-admin/',
    license = 'MIT',
    description = "Admin widgets for management very large data.",
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    packages = find_packages(),
    requires = [],
    include_package_data = True,
    zip_safe = False,
)
