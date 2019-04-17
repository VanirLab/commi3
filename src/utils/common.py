#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.


"""
from bs4.diagnose import diagnose
import re
import os
import sys
import json

import hashlib
import urllib.request, urllib.parse, urllib.error
import _thread
from urllib.request import urlopen
import traceback 
from src.utils import menu
from src.utils import settings
from socket import socket

# Use of this source code is governed by the MIT license.
__license__ = "MIT"

"""
Automatically create a Github issue with unhandled exception information.
PS: Greetz @ sqlmap dev team for that great idea! :)
"""
def create_github_issue(err_msg, exc_msg):
  
  key = hashlib.sha512()
  key.update(('%s%s' % (err_msg,exc_msg)).encode('utf-8'))
  password_hash = key.hexdigest()

  while True:
    try:
      if not menu.options.batch:
        question_msg = "Do you want to automatically create a new (anonymized) issue "
        question_msg += "with the unhandled exception information at "
        question_msg += "the official Github repository? [y/N] "
        sys.stdout.write(settings.print_question_msg(question_msg))
        choise = sys.stdin.readline().replace("\n","").lower()
      else:
        choise = ""
      if len(choise) == 0:
        choise = "n"
      if choise in settings.CHOICE_YES:
        break
      elif choise in settings.CHOICE_NO:
        print ("")
        return
      else:
        err_msg = "'" + choise + "' is not a valid answer."  
        print((settings.print_error_msg(err_msg)))
        pass
    except: 
      print ("\n")
      raise SystemExit()

  err_msg = err_msg[err_msg.find("\n"):]
  req = urllib.request.Request(url="https://api.github.com/search/issues?q=" + \
        urllib.parse("repo:VanirLab/commi3" + " " + "Unhandled exception (#" + str(key) + ")")
        )

  try:
    content = urllib.request.read()
    _ = json.loads(content)
    duplicate = _["total_count"] > 0
    closed = duplicate and _["items"][0]["state"] == "closed"
    if duplicate:
      warn_msg = "That issue seems to be already reported"
      if closed:
          warn_msg += " and resolved. Please update to the latest "
          warn_msg += "(dev) version from official GitHub repository at '" + settings.GIT_URL + "'"
      warn_msg += ".\n"   
      print((settings.print_warning_msg(warn_msg)))
      return
  except:
    pass

  data = {"title": "Unhandled exception (#" + str(key) + ")", "body": "```" + str(err_msg) + "\n```\n```\n" + str(exc_msg) + "```"}
  req = urllib.request.Request(url="https://api.github.com/repos/VaniLab/commi3/issues", data=json.dumps(data), headers={"Authorization": "token " + str(settings.GITHUB_REPORT_OAUTH_TOKEN.decode("base64"))})
  
  try:
    content = urllib.request.read()
    
  except err: # Handling Exceptions!
    print(content)
    content = None

  issue_url = re.search(r"https://github.com/VanirLab/commi3/issues/\d+", content or "")

  if issue_url:
    info_msg = "The created Github issue can been found at the address '" + str(issue_url.group(0)) + "'.\n"
    print((settings.print_info_msg(info_msg)))
  else:
    warn_msg = "Something went wrong while creating a Github issue."
    if "Unauthorized" in str(err):
      warn_msg += " Please update to the latest revision.\n"
    print((settings.print_warning_msg(warn_msg)))

"""
Masks sensitive data in the supplied message.
"""
def mask_sensitive_data(err_msg):
  for item in settings.SENSITIVE_OPTIONS:
    match = re.search(r"(?i)commi3.+("+str(item)+")(\s+|=)([^ ]+)", err_msg)
    if match:
      err_msg = err_msg.replace(match.group(3), '*' * len(match.group(3)))
  return err_msg

"""
Returns detailed message about occurred unhandled exception.
"""
def unhandled_exception():
  exc_msg = str(traceback.format_exc())

  if "bad marshal data" in exc_msg:
    match = re.search(r"\s*(.+)\s+ValueError", exc_msg)
    err_msg = "Identified corrupted .pyc file(s)."
    err_msg += "Please delete .pyc files on your system to fix the problem."
    print((settings.print_critical_msg(err_msg) ))
    raise SystemExit()

  elif "must be pinned buffer, not bytearray" in exc_msg:
    err_msg = "Error occurred at Python interpreter which "
    err_msg += "is fixed in 2.7.x. Please update accordingly. "
    err_msg += "(Reference: https://bugs.python.org/issue8104)"
    print((settings.print_critical_msg(err_msg)))
    raise SystemExit()

  elif "MemoryError" in exc_msg:
    err_msg = "Memory exhaustion detected."
    print((settings.print_critical_msg(err_msg)))
    raise SystemExit()

  elif any(_ in exc_msg for _ in ("No space left", "Disk quota exceeded")):
    err_msg = "No space left on output device."
    print((settings.print_critical_msg(err_msg)))
    raise SystemExit()

  elif "Read-only file system" in exc_msg:
    errMsg = "Output device is mounted as read-only."
    print((settings.print_critical_msg(err_msg)))
    raise SystemExit()

  elif "OperationalError: disk I/O error" in exc_msg:
    errMsg = "I/O error on output device."
    print((settings.print_critical_msg(err_msg)))
    raise SystemExit()

  else:
    err_msg = "Unhandled exception occurred in '" + settings.VERSION[1:] + "'. It is recommended to retry your "
    err_msg += "run with the latest (dev) version from official GitHub "
    err_msg += "repository at '" + settings.GIT_URL + "'. If the exception persists, please open a new issue "
    err_msg += "at '" + settings.ISSUES_PAGE + "' "
    err_msg += "with the following text and any other information required to "
    err_msg += "reproduce the bug. The "
    err_msg += "developers will try to reproduce the bug, fix it accordingly "
    err_msg += "and get back to you.\n"
    err_msg += "Commi3 version: " + settings.VERSION[1:] + "\n"
    err_msg += "Python version: " + settings.PYTHON_VERSION + "\n"
    err_msg += "Operating system: " + os.name + "\n"
    err_msg += "Command line: " + re.sub(r".+?\bcommi3\.py\b", "commi3.py", " ".join(sys.argv)) + "\n"
    err_msg = mask_sensitive_data(err_msg)
    exc_msg = re.sub(r'".+?[/\\](\w+\.py)', "\"\g<1>", exc_msg)
    print((settings.print_critical_msg(err_msg + "\n" + exc_msg.rstrip())))
    print((create_github_issue(err_msg, exc_msg)))
    

# eof
