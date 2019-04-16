#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""

import sys
from urllib.request import urlopen
#import httplib
import http.client
import urllib
import urllib3
from src.utils import (
    menu,
    settings,
)





from src.core.requests import headers
from colorama import Fore, Back, Style, init

# Use of this source code is governed by the MIT license.
__license__ = "MIT"

"""
 Check if HTTP Proxy is defined.
"""
def do_check(url):
  check_proxy = True
  try:
    if settings.VERBOSITY_LEVEL >= 1:
      info_msg = "Setting the HTTP proxy for all HTTP requests... "
      print (settings.print_info_msg(info_msg)) 
    # Check if defined POST data
    if menu.options.data:
      request = urllib.request.Request(url, menu.options.data)
    else:
       request = urllib.request.Request(url)
    # Check if defined extra headers.
    headers.do_check(request)
    request.set_proxy(menu.options.proxy,settings.PROXY_SCHEME)
    try:
      check = urllib.request.parse(request)
    except urllib.error.URLError as error:
      check = error
  except:
    check_proxy = False
    pass
  if check_proxy == True:
    pass
  else:
    err_msg = "Unable to connect to the target URL or proxy ("
    err_msg += menu.options.proxy
    err_msg += ")."
    print (settings.print_critical_msg(err_msg))
    raise sys.exit()
    
"""
Use the defined HTTP Proxy
"""
def use_proxy(request):
  headers.do_check(request)
  request.set_proxy(menu.options.proxy,settings.PROXY_SCHEME)
  try:
    response = urlopen(request)
    return response

  except httplib.BadStatusLine as e:
    err_msg = "Unable to connect to the target URL or proxy ("
    err_msg += menu.options.proxy
    err_msg += ")."
    print (settings.print_critical_msg(err_msg))
    raise sys.exit() 

  except Exception as err_msg:
    try:
      error_msg = str(err_msg.args[0]).split("] ")[1] + "."
    except IndexError:
      error_msg = str(err_msg).replace(": "," (") + ")."
    print (settings.print_critical_msg(error_msg))
    raise sys.exit()

# eof 