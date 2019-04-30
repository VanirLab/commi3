#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""

from __future__ import absolute_import
from __future__ import print_function
import sys
import base64
import urllib.request, urllib.parse, urllib.error
from src.utils import settings

"""
About: Base64 all characters in a given payload.
Notes: This tamper script works against all targets.
"""

__tamper__ = "base64encode"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  if settings.WHITESPACE[0] == "+":
    err_msg = "Tamper script '" +  __tamper__  + "' is unlikely to work combined with the tamper script 'space2plus'."
    if settings.VERBOSITY_LEVEL == 0:
      print ("")
    print((settings.print_critical_msg(err_msg))) 
    raise SystemExit()

  else:
    payload = urllib.parse.unquote(payload)
    payload = base64.b64encode(payload)
    return payload

# eof 