#!/usr/bin/env python
# encoding: UTF-8

import sqlite3
import sys

"""
Show version number and exit.
"""
def show_version():
  from src.utils import settings
  print(settings.VERSION)
  raise SystemExit()

"""
Check python version number.
"""
def python_version():
  PYTHON_VERSION = sys.version.split()[0]
  if PYTHON_VERSION <"3.7":
    err_msg = "[x] Critical: Incompatible Python version (" 
    err_msg += PYTHON_VERSION + ") detected. "
    err_msg += "Use Python version 2.6.x or 2.7.x.\n"
    print(err_msg)
    raise SystemExit()
  """
  Reach sql connection.
  """  
def python_sql():
  PYTHON_SQ3 = sqlite3.connect('db')
  if PYTHON_SQ3:
    err_msg = "No connection"
    print(err_msg)
    
    return 0
  
  
    
