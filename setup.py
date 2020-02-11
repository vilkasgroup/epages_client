#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "requests",
    "validators"
]

setup_requirements = [
    'pytest-runner',
    # TODO(spexii): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='epages_client',
    version='0.2.0',
    description="Python client for ePages REST API.",
    long_description=readme + '\n\n' + history,
    author="Pekka Piispanen, Tero Kotti",
    author_email='pekka@vilkas.fi, tero@vilkas.fi',
    url='https://github.com/vilkasgroup/epages_client',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='epages_client',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
