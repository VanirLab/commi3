#!/usr/bin/env python3
# encoding: UTF-8

"""

This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.
"""
# Use of this source code is governed by the MIT license.
__license__ = "MIT"
from .src.core import main


try:
  __import__("src.utils.version")
  from .src.utils import version
  version.python_version()
  

except ImportError:
  err_msg = "Wrong installation detected (missing modules). "
  err_msg = "Visit 'https://github.com/VanirLab/commi3/' for further details. \n"
  print((settings.print_critical_msg(err_msg)))
  raise SystemExit()

# Main
if __name__ == '__main__':
  try:
    import sys
    from .src.core import main

  except PendingDeprecationWarning:
    import sys
    raise Warning()
    #print(SystemError)
  
  
  except SystemExit:
    import sys
    raise SystemExit() 

  except KeyboardInterrupt:
    import sys
    raise SystemExit() 
  
  except Warning:
    import sys
    raise SystemExit()
  
  except:
    from .src.utils import common
    raise common.unhandled_exception()

# eof
