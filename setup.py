# -*- coding: utf-8 -*-
from setuptools import setup

name = "bulbs-component-external-link"
version = "0.0.1"

requires = [
    "django-bulbs==0.6.1",
]

dev_requires = [
    "virtualenv==13.0.3"
]

setup(
    name=name,
    version=version,
    description="External Link component for bulbs.",
    license="MIT",
    author="Andrew Kos",
    author_email="akos@theonion.com",
    package_dir={
        "bulbs_component_external_link": "src/django-bulbs",
        "bulbs_component_external_link_cms": "compat-builds/django-bulbs-cms"
    },
    packages=[
        "bulbs_component_external_link",
        "bulbs_component_external_link_cms"
    ],
    include_package_data=True,
    install_requires=requires,
    extras_require={
        "dev": dev_requires
    }
)
