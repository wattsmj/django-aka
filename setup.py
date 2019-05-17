'''
Smart Bookmark Tool that redirects your web browser based on labels
Copyright (C) 2019  Matthew Watts

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Author: wattsmj
Contact: Please raise an issue on www.github.com/wattsmj/django-aka
Description: Package installation file
'''

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-aka',
    version='0.1.0',
    author='wattsmj',
    license='GPL-3.0',
    url='https://github.com/wattsmj/django-aka',
    description='A smart bookmarking Django app',
    long_description=README,
    packages=find_packages(),
    install_requires=['django', 'fuzzywuzzy'],
    include_package_data=True
)