#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""

import random
from src.utils import settings

"""
About: Adds multiple spaces around OS commands
Notes: Useful to bypass very weak and bespoke web application firewalls that has poorly written permissive regular expressions.
"""

__tamper__ = "multiplespaces"

settings.TAMPER_SCRIPTS[__tamper__] = True
settings.WHITESPACE[0] = settings.WHITESPACE[0] * random.randrange(2, 8)

# eof 