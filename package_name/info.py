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
__url__ = 'Repository URL'
__license__ = 'MIT'
__description__ = 'Short description of your package'
__about__ = (f'{__name__} \n\n '
             'Author: {__author__} \n '
             'Year: Current Year \n '
             'Email: Your Email Address \n '
             'Website: Your Website URL \n\n '
             'A longer description of what your package does \n\n')
__requires__ = []  # Your package dependencies
__setup_requires__ = ['pytest-runner', ]
__tests_require__ = ['pytest', 'pytest-cov', 'pytest-pep8']
