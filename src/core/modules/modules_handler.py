#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""



import os
import sys

from src.utils import menu
from src.utils import settings
from colorama import Fore, Back, Style, init

"""
Load modules
"""
def load_modules(url, http_request_method, filename):

  # Check if defined the ICMP exfiltration module
  if menu.options.ip_icmp_data :
    try:
      # The ICMP exfiltration module
      from src.core.modules.icmp_exfiltration import icmp_exfiltration
      # The ICMP exfiltration handler
      icmp_exfiltration.icmp_exfiltration_handler(url, http_request_method)
    except ImportError as err_msg:
      print ("\n" + settings.print_critical_msg(err_msg))
      raise sys.exit() 
    raise sys.exit()

  # Check if defined the DNS exfiltration module
  if menu.options.dns_server :
    try:
      # The DNS exfiltration module
      from src.core.modules.dns_exfiltration import dns_exfiltration
      # The DNS exfiltration handler
      dns_exfiltration.dns_exfiltration_handler(url, http_request_method)
    except ImportError as err_msg:
      print ("\n" + settings.print_critical_msg(err_msg))
      raise sys.exit() 
    raise sys.exit()

  # Check if defined the shellshock module
  if menu.options.shellshock :
    try:
      # The shellshock module
      from src.core.modules.shellshock import shellshock
      # The shellshock handler
      shellshock.shellshock_handler(url, http_request_method, filename)
    except ImportError as err_msg:
      print ("\n" + settings.print_critical_msg(err_msg))
      raise sys.exit() 
    raise sys.exit() 