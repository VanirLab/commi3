#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.
"""

from random import sample
from src.utils import settings

"""
About: Appends a fake HTTP header 'X-Forwarded-For'.
"""

__tamper__ = "xforwardedfor"
settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(request):
  def randomIP():
    numbers = []
    while not numbers or numbers[0] in (10, 172, 192):
      numbers = sample(range(1, 255), 4)
    return '.'.join(str(_) for _ in numbers)

  request.add_header('X-Forwarded-For', randomIP())
  request.add_header('X-Client-Ip', randomIP())
  request.add_header('X-Real-Ip', randomIP())

# eof 