# -*- coding: utf-8 -*-

"""PACKAGE INFO

This module provides some basic information about the package.

"""

# Set the package release version
version_info = (0, 0, 0)
__version__ = '.'.join(str(c) for c in version_info)

# Set the package details
__author__ = 'Your Name'
__email__ = 'Your Email Address'
__year__ = '2019'
__url__ = 'Repository URL'
__description__ = 'Short description of your package'
__long_description__ = 'A longer description of your package'
__requires__ = []  # Your package dependencies

# Default package properties
__license__ = 'MIT'
__about__ = (f'{__name__} \n\n '
             'Author: {__author__} \n '
             'Email: {__email__} \n '
             'Year: {__year__} \n '
             '{__long_description__} \n\n')
__setup_requires__ = ['pytest-runner', ]
__tests_require__ = ['pytest', 'pytest-cov', 'pytest-pep8']
