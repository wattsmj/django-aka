import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-aka',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='',
    description='A smart bookmarking Django app',
    long_description=README,
    url='',
    author='wattsmj',
    author_email='',
    install_requires=['django', 'fuzzywuzzy']
)