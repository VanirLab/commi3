#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""

import sys
import os
import logging



#ENUMs
PLATFORM = os.name 
#IS_WINDOWS = hasattr(sys, "getwindowsversion")
IS_WINDOWS = PLATFORM == "nt"

_readline = None

try:
    from readline import *
    import readline as _readline
except:
    try:
        from pyreadline import *
        import pyreadline as _readline
    except:
        pass

if IS_WINDOWS and _readline:
    try:
        _outputfile = _readline.GetOutputFile()
    except AttributeError:
        debugMsg = "Failed GetOutputFile when using platform's "
        debugMsg += "readline library"
        logger.debug(debugMsg)

        _readline = None

# Test to see if libedit is being used instead of GNU readline.
# Thanks to Boyd Waters for this patch.
uses_libedit = False

if PLATFORM == 'mac' and _readline:
    import subprocess

    (status, result) = subprocess.getstatusoutput("otool -L %s | grep libedit" % _readline.__file__)

    if status == 0 and len(result) > 0:
        # We are bound to libedit - new in Leopard
        _readline.parse_and_bind("bind ^I rl_complete")

        debugMsg = "Leopard libedit detected when using platform's "
        debugMsg += "readline library"
        logger.debug(debugMsg)

        uses_libedit = True

# the clear_history() function was only introduced in Python 2.4 and is
# actually optional in the readline API, so we must explicitly check for its
# existence.  Some known platforms actually don't have it.  This thread:
# http://mail.python.org/pipermail/python-dev/2003-August/037845.html
# has the original discussion.
if _readline:
    if not hasattr(_readline, "clear_history"):
        def clear_history():
            pass

        _readline.clear_history = clear_history