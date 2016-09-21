#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    "requests",
    "bs4",
    "lxml"
]

setup(
    name='parivahan-py',
    version='0.1.0',
    description="Get Vehicle Details from Registration Number from parivahan.gov site",
    long_description=readme,
    author="Suraj Arya",
    author_email='suraj@loanzen.in',
    url='https://github.com/suraj-arya/parivahan',
    packages=[
        'parivahan',
    ],
    package_dir={'parivahan':
                 'parivahan'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='parivahan',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ]
)