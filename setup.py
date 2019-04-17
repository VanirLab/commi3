#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.
"""
import re
import ast
from setuptools import setup, Extension

cversion = re.compile(r'__version__\s+=\s+(.*)')
with open('commi3.py') as f:
 version = "1.0.0"


 setup(
  name='Commi3',
  version=version,
  url='http://github.com/VanirLab/commi3/',
  license='MIT',
  author='Chris Pro',
  description='is an Automated Commando Line Tool for pentest',
  long_description=__doc__,
  url="https://github.com/VanirLab/commi3",
  #ext_modules=[Extension('commi3',sources=['settings.c'])], #Import your own C/C++ packages
  #packages=['src'],
  package_dir={'':'src/utils'},
  package_data={'': ['core/*.py']},
  include_package_data=True,
  packages=setuptools.find_packages()
  zip_safe=False,
  platforms='any',
  install_requires=[
  'colorama',
  'Jinja2',
  'dns-lexicon',
  'bs4',
  ],
  classifiers=[
  'Development Status :: Commi3 - Beta',
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
