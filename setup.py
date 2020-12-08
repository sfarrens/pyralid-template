#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# Set the package release version
major = 0
minor = 0
patch = 0

# Set the package details
name = 'configure_package_name'
version = '.'.join(str(value) for value in (major, minor, patch))
author = 'configure_author'
email = 'configure_email'
gh_user = 'configure_ghuser'
url = 'https://github.com/{0}/{1}'.format(gh_user, name)
year = 'configure_year'
description = 'configure_description'

# Set package summary
summary = ('{} Author: {}, Email: {}, Year: {}, Description: {}'
           ''.format(name, author, email, year, description))

# Source package description from README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Source package requirements from requirements.txt
with open('requirements.txt') as open_file:
    install_requires = open_file.read()

# Source test requirements from develop.txt
with open('develop.txt') as open_file:
    tests_require = open_file.read()

# Source doc requirements from docs/requirements.txt
with open('docs/requirements.txt') as open_file:
    docs_require = open_file.read()


# Find scripts
def find_scripts():

    sdir = 'scripts'

    return [os.path.join(sdir, val) for val in os.listdir(sdir) if
            val.endswith('.py') and '__init__' not in val]


setup(
    name=name,
    author=author,
    author_email=email,
    version=version,
    license='MIT',
    url=url,
    description=summary,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    scripts=find_scripts(),
    install_requires=install_requires,
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    extras_require={'develop': tests_require + docs_require}
)
