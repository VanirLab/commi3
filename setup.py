#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.
"""
import re
import os
import ast
from setuptools import setup, Extension
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

cversion = re.compile(r'__version__\s+=\s+(.*)')
with open('commi3.py') as f:
 version = "1.0.5"
 
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
 README = readme.read()
 
    


 setup(
  name='Commi3',
  version=version,
  license='MIT',
  author='Chris Pro',
  description='Is an Automated Commando Line Tool for pentesting and other fun stuff',
  long_description_content_type="text/markdown",
  long_description=README,
  url="https://github.com/VanirLab/commi3",
  #ext_modules=[Extension('commi3',sources=['settings.c'])], #Import your own C/C++ packages
  #packages=['src'],
  package_dir={'':'src/utils'},
  package_data={'': ['core/*.py']},
  include_package_data=True,
  #packages=setuptools.find_packages(),
  zip_safe=False,
  platforms='any',
  install_requires=[
  'colorama',
  'Jinja2',
  'dns-lexicon',
  'bs4',
  ],
  classifiers=[
  'Environment :: Web Environment',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Operating System :: OS Independent',
  'Programming Language :: Python',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.3',
  'Programming Language :: Python :: 3.4',
  'Programming Language :: Python :: 3.5',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
  'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
  'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  entry_points='''
  [console_scripts]
  commi3=commi3.cli:main
  '''
 )
