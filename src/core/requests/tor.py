#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.


# [NOTES] -----------------------------------------------------------
# 1) Tested on Linux (Ubuntu), Windows 10, and Mac OS X
# 2) If the script is slowing down or freezes, make sure you have TOR running on the 
#        specified TOR_PORT
#--------------------------------------------------------------------

"""

import re
import os
import sys
import time
import urllib.request, urllib.parse, urllib.error
import random
import html5lib
import socket
import socks


from urllib.request import urlopen
#import httplib
import http.client
from optparse import OptionParser
from src.utils import menu 
from src.utils import settings 
from src.utils import requirments
from colorama import Fore, Back, Style, init

"""
Check for TOR HTTP Proxy.
"""
#SocksListenAddress
TOR_SERVER = "127.0.0.1"
#SocksListenAddress2
TOR_SOCK_SERVER = "0.0.0.0"

#SOCKS connections on port
TOR_PORT = 9050

#Tor Browser listens on port 
TOR_LIS_PORT = 9150

#Reachable Addresses expoMode
REACH_DIR_ADDRESS= int(80)
REACH_OR_ADDRESS= int(443)

tor_port = 9150

headers = {
'Accept' : '*/*',
}

"""
Enable IPv6: To activate it enable this function
"""
CLIENT_USE_IPv4 = 0
CLIENT_USE_IPv6 = 1
"""
Limit the total amount of bandwidth
"""
RELAY_BANDWIDTH_RATE = 1000
RELAY_BANDWIDTH_BUFFER = 1000 # allow higher buffer but not recommended
RELAY_BANDWIDTH_BURTS = 5000 # allow higher bursts but maintain average

user_agents = [
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; )',
'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-GB; rv:1.8.1.18) Gecko/20081029 Firefox/2.0.0.18',
'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
'Opera/9.51 (Macintosh; Intel Mac OS X; U; en)',
'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.2.1; MultiZilla v1.1.32 final) Gecko/20021130',
]

if tor_port:
  PRIVOXY_PORT = tor_port
  #reload(PRIVOXY_PORT = tor_port)
elif opts.random:
  random.seed(time.time())
  headers['User-Agent'] = random.choice(user_agents)
  #print(tor_port.__all__)
else:
  PRIVOXY_PORT = settings.PRIVOXY_PORT

"""
Check if HTTP Proxy (tor/privoxy) is defined.
"""
def do_check():

  # Check if 'tor' is installed.
  requirment = "tor"
  requirments.do_check(requirment)

  # Check if 'privoxy' is installed.
  requirment = "privoxy"
  requirments.do_check(requirment)
    
  check_privoxy_proxy = True
  info_msg = "Testing Tor SOCKS proxy settings (" 
  info_msg += settings.PRIVOXY_IP + ":" + PRIVOXY_PORT 
  info_msg +=  ")... "
  sys.stdout.write(settings.print_info_msg(info_msg))
  sys.stdout.flush()
  try:
    privoxy_proxy = urllib.request.ProxyHandler({settings.SCHEME:settings.PRIVOXY_IP + ":" + PRIVOXY_PORT})
    opener = urllib.request.build_opener(privoxy_proxy)
    urllib.request.install_opener(opener)
  except:
    check_privoxy_proxy = False
    pass
    
  if check_privoxy_proxy:
    try:
      check_tor_page = opener.open("https://check.torproject.org/").read()
      found_ip = re.findall(r":  <strong>" + "(.*)" + "</strong></p>", check_tor_page)
      if not "You are not using Tor" in check_tor_page:
        sys.stdout.write("[" + Fore.GREEN + " SUCCEED " + Style.RESET_ALL + "]\n")
        sys.stdout.flush()
        if menu.options.tor_check:
          success_msg = "Tor connection is properly set. "
        else:
          success_msg = ""
        success_msg += "Your ip address appears to be " + found_ip[0] + ".\n"
        sys.stdout.write(settings.print_success_msg(success_msg))
        warn_msg = "Increasing default value for option '--time-sec' to"
        warn_msg += " " + str(settings.TIMESEC) + " because switch '--tor' was provided."
        print((settings.print_warning_msg(warn_msg)))

      else:
        print(("[" + Fore.RED + " FAILED " + Style.RESET_ALL + "]"))
        if menu.options.tor_check:
          err_msg = "It seems that your Tor connection is not properly set. "
        else:
          err_msg = "" 
        err_msg += "Can't establish connection with the Tor SOCKS proxy. "
        err_msg += "Please make sure that you have "
        err_msg += "Tor installed and running so "
        err_msg += "you could successfully use "
        err_msg += "switch '--tor'."
        print((settings.print_critical_msg(err_msg)))  
        raise sys.exit() 

    except urllib.error.URLError as err_msg:
      print(("[" + Fore.RED + " FAILED " + Style.RESET_ALL + "]"))
      if menu.options.tor_check:
        err_msg = "It seems that your Tor connection is not properly set. "
      else:
        err_msg = ""
      err_msg = "Please make sure that you have "
      err_msg += "Tor installed and running so "
      err_msg += "you could successfully use "
      err_msg += "switch '--tor'."
      print((settings.print_critical_msg(err_msg)))  
      raise sys.exit()  

    except httplib.BadStatusLine as err_msg:
      print(("[ " + Fore.RED + "FAILED" + Style.RESET_ALL + " ]"))
      if len(err_msg.line) > 2 :
        print((err_msg.line, err_msg.message))
      raise sys.exit()


"""
Use the TOR HTTP Proxy.
"""
def use_tor(request):
  if menu.options.offline:  
    err_msg = "You cannot Tor network without access on the Internet."
    print((settings.print_critical_msg(err_msg)))
    raise sys.exit()
    
  try:
    privoxy_proxy = urllib.request.ProxyHandler({settings.SCHEME:settings.PRIVOXY_IP + ":" + PRIVOXY_PORT})
    opener = urllib.request.build_opener(privoxy_proxy)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(request)
    return response

  except Exception as err_msg:
    try:
      error_msg = str(err_msg.args[0]).split("] ")[1] + "."
    except IndexError:
      error_msg = str(err_msg).replace(": "," (") + ")."
    print((settings.print_critical_msg(error_msg)))
    raise sys.exit()
  
  
  if __name__ == 'do_check':
    use_tor()
    do_check()

# eof 