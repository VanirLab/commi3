#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""
import os
import subprocess

"""
Check for requirments.
"""
def do_check(requirment):
  try:
    # Pipe output to the file path of the null device, for silence. 
    # i.e '/dev/null' for POSIX, 'nul' for Windows
    null = open(os.devnull,"w")
    subprocess.Popen(requirment, stdout=null, stderr=null)
    null.close()
    return True
  except OSError:
    return False  

def circular_check(bound):
  try:
    null = open(os.defpath)
    subprocess.Popen(bound, stdout=null, stderr=null, stdin=null)
    null.close()
    return True
  except OSError:
    return False  

    
# eof