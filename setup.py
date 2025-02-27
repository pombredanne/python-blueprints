#!/usr/bin/env python
from setuptools import setup


setup(
    name='Blueprints',
    version='2.3.0.2',
    url='https://github.com/python-graph-lovestory/python-blueprints',
    license='BSD',
    author='Amirouche Boubekki',
    author_email='amirouche.boubekki@gmail.com',
    description="Python bindings of Tinkerpop's Blueprints",
    packages=('blueprints', 'blueprints.javalib'),
    include_package_data=True,
    package_data={
        '': ['*.jar'],
    },
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
