#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.
"""

from src.utils import settings

"""
About: Replaces space character ('%20') with vertical tab ('%0b').
Notes: This tamper script works against Windows targets.
"""

__tamper__ = "space2vtab"

if settings.TARGET_OS == "win":
  settings.TAMPER_SCRIPTS[__tamper__] = True
  if settings.WHITESPACE[0] == "%20":
    settings.WHITESPACE[0] = "%0b"
  else:
    settings.WHITESPACE.append("%0b") 
else:
  warn_msg = "Unix target host(s), does not support vertical tab(s)."
  print (settings.print_warning_msg(warn_msg))

# eof 