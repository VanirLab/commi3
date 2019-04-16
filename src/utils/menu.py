#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""
import queue
import os
import sys
import re

import getopt
import shlex
import logging
import argparse
#urllibInject
import urllib.request, urllib.parse, urllib.error
import urllib.parse


from urllib.request import urlopen
from pyfiglet import Figlet
from optparse import OptionError
from optparse import OptionGroup
from optparse import OptionParser
from optparse import SUPPRESS_HELP

from src.utils import settings
from colorama import Fore, Back, Style, init


# Use Colorama to make Termcolor work on Windows too :)


"""
The commi3 banner.
"""
def banner(self, banner, info):
  self._banner = sanitizeStr(banner)
  self._inVersion = False
  self._inServicePack = False
  self._release = None
  self._version = ""
  self._versionAlt = None
  self._servicePack = ""
  self._info = inf  
  ascii_banner = Figlet(font='starwars')
  
  #print(ascii_banner.renderText('Commi3'))
  #print(Back.WHITE, ascii_banner, Fore.BLACK + Style.DIM)  
  print((Back.RED + Fore.WHITE + Style.DIM + ascii_banner.renderText('Commi3') + Style.RESET_ALL+ 
         Fore.WHITE + settings.VERSION + "-----" +
         Style.RESET_ALL +   Fore.WHITE +
         Style.DIM + settings.APPLICATION_URL
         + Style.RESET_ALL + 
         Fore.LIGHTRED_EX + Style.RESET_ALL +
         """) +-- """ + Style.BRIGHT + settings.DESCRIPTION_FULL + Style.RESET_ALL + """ Copyright © """ + settings.YEAR
         + """ """ + settings.AUTHOR + Style.RESET_ALL + 
         """ (""" + Fore.LIGHTRED_EX  + Style.RESET_ALL + """) +--
"""))

_ = os.path.normpath(sys.argv[0])

#DEFAULT_TOR_PORT
tor_port = 9150
IS_WINDOWS = hasattr(sys, "getwindowsversion")
# URL used in Zombie runs
ZOMBIE_URL = "http://foo/bar?filename=zombie"


usage = "%s%s [options]" % ("python " if not IS_WINDOWS else "", \
            "\"%s\"" % _ if " " in _ else _)

parser = OptionParser(usage=usage)

# General options
general = OptionGroup(parser, Style.BRIGHT + Style.DIM + "General" + Style.RESET_ALL, 
                        "These options relate to general matters. ")

general.add_option("-v",
                default="0",
                action="store",
                type="int",
                dest="verbose",
                help="Verbosity level (0-4, Default: 0).")

general.add_option("--install",
                action="store_true",
                dest="install",
                default=False,
                help="Install 'commi3' to your system.")

general.add_option("--version",
                action="store_true",
                dest="version",
                help="Show version number and exit.")

general.add_option("--update", 
                action="store_true",
                dest="update",
                help="Check for updates (apply if any) and exit.")

general.add_option("--output-dir", 
                action="store",
                dest="output_dir",
                help="Set custom output directory path.")

general.add_option("-s", 
                action="store",
                dest="session_file",
                default=None,
                help="Load session from a stored (.sqlite) file.")

general.add_option("--flush-session",
                action="store_true",
                dest="flush_session",
                help="Flush session files for current target.")

general.add_option("--ignore-session", 
                action="store_true",
                dest="ignore_session",
                help="Ignore results stored in session file.")

general.add_option("-t",
                action="store",
                dest="traffic_file",
                default=None,
                help="Log all HTTP traffic into a textual file.")

general.add_option("--batch",
                action="store_true",
                dest="batch",
                default=False,
                help="Never ask for user input, use the default behaviour.")

general.add_option("--encoding",
                action="store",
                dest="encoding",
                default=None,
                help="Force character encoding used for data retrieval (e.g. GBK).")

general.add_option("--charset",
                action="store",
                dest="charset",
                default=None,
                help="Time-related injection charset (e.g. \"0123456789abcdef\")")

general.add_option("--check-internet", 
                action="store_true",
                dest="check_internet",
                help="Check internet connection before assessing the target.")

# Target options
target = OptionGroup(parser, Style.BRIGHT + Style.DIM + "Target" + Style.RESET_ALL, 
                     "This options has to be provided, to define the target URL. ")

target.add_option("-u","--url",
                action="store",
                dest="url",
                help="Target URL.")
                
target.add_option("--url-reload",
                action="store_true",
                dest="url_reload",
                default=False,
                help="Reload target URL after command execution.")

target.add_option("-l",
                dest="logfile",
                help="Parse target from HTTP proxy log file.")

target.add_option("--d9","--direct", dest="direct", help="Connection string "
                  "for direct database connection")

target.add_option("-m",
                dest="bulkfile",
                help="Scan multiple targets given in a textual file.")

target.add_option("-r",
                dest="requestfile",
                help="Load HTTP request from a file.")

target.add_option("--crawl", 
                dest="crawldepth",
                type="int",
                help="Crawl the website starting from the target URL (1-2, Default: " + str(settings.DEFAULT_CRAWLDEPTH_LEVEL) + ").")

target.add_option("-x",
                dest="sitemap_url",
                help="Parse target(s) from remote sitemap(.xml) file.")

target.add_option("-g", dest="googledork",
                  help="Process Google dork results as target URLs")

# Request options
request = OptionGroup(parser,  Style.BRIGHT + Style.DIM + "Request" + Style.RESET_ALL, 
                      "These options can be used to specify how to connect to the target URL.")


request.add_option("-d", "--data", 
                action="store",
                dest="data",
                default=False,
                help="Data string to be sent through POST.")

request.add_option("--host",
                action="store",
                dest="host",
                help="HTTP Host header.")

request.add_option("--referer",
                action="store",
                dest="referer",
                help="HTTP Referer header.")

request.add_option("--user-agent",
                action="store",
                dest="agent",
                default = settings.DEFAULT_USER_AGENT,
                help="HTTP User-Agent header.")

request.add_option("--random-agent",
                action="store_true",
                dest="random_agent",
                default=False,
                help="Use a randomly selected HTTP User-Agent header.")

request.add_option("--param-del",
                action="store",
                dest="pdel",
                help="Set character for splitting parameter values.")

request.add_option("--cookie",
                action="store",
                dest="cookie",
                help="HTTP Cookie header.")

request.add_option("--cookie-del",
                action="store",
                dest="cdel",
                help="Set character for splitting cookie values.")

request.add_option("-H","--header",
                action="store",
                dest="header",
                help="Extra header (e.g. 'X-Forwarded-For: 127.0.0.1').")

request.add_option("--headers",
                action="store",
                dest="headers",
                help="Extra headers (e.g. 'Accept-Language: fr\\nETag: 123').")

request.add_option("--proxy",
                action="store",
                dest="proxy",
                default=False,
                help="Use a proxy to connect to the target URL.")
                
request.add_option("--tor",
                action="store_true",
                dest="tor",
                default=False,
                help="Use the Tor network.")

request.add_option("--tor-port",
                action="store",
                dest="tor_port",
                default=False,
                help="Set Tor proxy port (Default: 9150).")

request.add_option("--tor-check",
                action="store_true",
                dest="tor_check",
                default=False,
                help="Check to see if Tor is used properly.")

request.add_option("--auth-url",
                action="store",
                dest="auth_url",
                help="Login panel URL.")

request.add_option("--auth-data",
                action="store",
                dest="auth_data",
                help="Login parameters and data.")

request.add_option("--auth-type",
                action="store",
                dest="auth_type",
                help="HTTP authentication type (e.g. 'Basic' or 'Digest').")

request.add_option("--auth-cred",
                action="store",
                dest="auth_cred",
                help="HTTP authentication credentials (e.g. 'admin:admin').")

request.add_option("--ignore-401",
                action="store_true",
                dest="ignore_401",
                default=False,
                help="Ignore HTTP error 401 (Unauthorized).")

request.add_option("--force-ssl",
                action="store_true",
                dest="force_ssl",
                default=False,
                help="Force usage of SSL/HTTPS.")

request.add_option("--ignore-redirects",
                action="store_true",
                dest="ignore_redirects",
                default=False,
                help="Ignore redirection attempts.")

request.add_option("--retries",
                action="store",
                dest="retries",
                default=False,
                type="int",
                help="Retries when the connection timeouts (Default: 3).")

# Enumeration options DIM _> DIM
enumeration = OptionGroup(parser, Style.BRIGHT + Style.DIM + "Enumeration" + Style.RESET_ALL, 
                        "These options can be used to enumerate the target host.")

enumeration.add_option("--all", 
                action="store_true",
                dest="enum_all",
                default=False,
                help="Retrieve everything.")

enumeration.add_option("--current-user", 
                action="store_true",
                dest="current_user",
                default=False,
                help="Retrieve current user name.")

enumeration.add_option("--hostname", 
                action="store_true",
                dest="hostname",
                default=False,
                help="Retrieve current hostname.")

enumeration.add_option("--is-root", 
                action="store_true",
                dest="is_root",
                default=False,
                help="Check if the current user have root privileges.")

enumeration.add_option("--is-admin", 
                action="store_true",
                dest="is_admin",
                default=False,
                help="Check if the current user have admin privileges.")

enumeration.add_option("--sys-info", 
                action="store_true",
                dest="sys_info",
                default=False,
                help="Retrieve system information.")

enumeration.add_option("--users", 
                action="store_true",
                dest="users",
                default=False,
                help="Retrieve system users.")

enumeration.add_option("--passwords", 
                action="store_true",
                dest="passwords",
                default=False,
                help="Retrieve system users password hashes.")

enumeration.add_option("--privileges", 
                action="store_true",
                dest="privileges",
                default=False,
                help="Retrieve system users privileges.")

enumeration.add_option("--ps-version", 
                action="store_true",
                dest="ps_version",
                default=False,
                help="Retrieve PowerShell's version number.")

# File access options
file_access = OptionGroup(parser, Style.BRIGHT + Style.DIM + "File access" + Style.RESET_ALL, 
                        "These options can be used to access files on the target host.")

file_access.add_option("--file-read", 
                action="store",
                dest="file_read",
                help="Read a file from the target host.")

file_access.add_option("--file-write", 
                action="store",
                dest="file_write",
                help="Write to a file on the target host.")

file_access.add_option("--file-upload", 
                action="store",
                dest="file_upload",
                help="Upload a file on the target host.")

file_access.add_option("--file-dest", 
                action="store",
                dest="file_dest",
                help="Host's absolute filepath to write and/or upload to.")

# Modules options
modules = OptionGroup(parser, Style.BRIGHT + Style.DIM + "Modules" + Style.RESET_ALL, 
                        "These options can be used increase the detection and/or injection capabilities.")
modules.add_option("--icmp-exfil", 
                action="store",
                dest="ip_icmp_data",
                default=False,
                help="The 'ICMP exfiltration' injection module.           (e.g. 'ip_src=192.168.178.1,ip_dst=192.168.178.3').")

modules.add_option("--dns-server", 
                action="store",
                dest="dns_server",
                default=False,
                help="The 'DNS exfiltration' injection module.        (Domain name used for DNS exfiltration attack).")

modules.add_option("--shellshock", 
                action="store_true",
                dest="shellshock",
                default=False,
                help="The 'shellshock' injection module.")

# Injection options
injection = OptionGroup(parser, Style.BRIGHT + Style.DIM + "Injection" + Style.RESET_ALL, 
                        "These options can be used to specify which parameters to inject and to provide custom injection payloads.")

injection.add_option("-p",
                action="store",
                dest="test_parameter",
                help="Testable parameter(s).")

injection.add_option("--skip", 
                action="store",
                dest="skip_parameter",
                help="Skip testing for given parameter(s).")

injection.add_option("--suffix", 
                action="store",
                dest="suffix",
                help="Injection payload suffix string.")

injection.add_option("--prefix", 
                action="store",
                dest="prefix",
                help="Injection payload prefix string.")

injection.add_option("--technique", 
                action="store",
                dest="tech",
                help="Specify injection technique(s) to use.")

injection.add_option("--skip-technique", 
                action="store",
                dest="skip_tech",
                help="Specify injection technique(s) to skip.")

injection.add_option("--maxlen", 
                action="store",
                dest="maxlen",
                default=settings.MAXLEN,
                help="Set the max length of output for time-related injection techniques (Default: " + str(settings.MAXLEN) + " chars).")

injection.add_option("--delay", 
                action="store",
                type="int",
                dest="delay",
                help="Seconds to delay between each HTTP request.")

injection.add_option("--time-sec", 
                action="store",
                type="int",
                dest="timesec",
                help="Seconds to delay the OS response (Default 1).")

injection.add_option("--tmp-path", 
                action="store",
                dest="tmp_path",
                default=False,
                help="Set the absolute path of web server's temp directory.")

injection.add_option("--web-root", 
                action="store",
                dest="web_root",
                default=False,
                help="Set the web server document root directory (e.g. '/var/www').")

injection.add_option("--alter-shell", 
                action="store",
                dest="alter_shell",
                default = "",
                help="Use an alternative os-shell (e.g. 'Python').")

injection.add_option("--os-cmd", 
                action="store",
                dest="os_cmd",
                default=False,
                help="Execute a single operating system command.")

injection.add_option("--os",
                action="store", 
                dest="os",
                default=False,
                help="Force back-end operating system (e.g. 'Windows' or 'Unix').")

injection.add_option("--tamper", 
                action="store",
                dest="tamper",
                default=False,
                help="Use given script(s) for tampering injection data.")

injection.add_option("--msf-path", 
                action="store",
                dest="msf_path",
                default=False,
                help="Set a local path where metasploit is installed.")

injection.add_option("--backticks", 
                action="store_true",
                dest="enable_backticks",
                default=False,
                help="Use backticks instead of \"$()\", for commands substitution.")

# Detection options
detection = OptionGroup(parser, Style.BRIGHT + Style.DIM + "Detection" + Style.RESET_ALL, "These options can be "
                        "used to customize the detection phase.")

detection.add_option("--level", 
                dest="level", 
                type="int",
                default=1,
                help="Level of tests to perform (1-3, Default: " + str(settings.DEFAULT_INJECTION_LEVEL) + ").")

detection.add_option("--skip-calc", 
                action="store_true",
                dest="skip_calc",
                default=False,
                help="Skip the mathematic calculation during the detection phase.")

detection.add_option("--skip-empty", 
                action="store_true",
                dest="skip_empty",
                default=False,
                help="Skip testing the parameter(s) with empty value(s).")

detection.add_option("--failed-tries", 
                action="store",
                dest="failed_tries",
                default=20,
                help="Set a number of failed injection tries, in file-based technique.")

# Miscellaneous options
misc = OptionGroup(parser, Style.BRIGHT + Style.DIM + "Miscellaneous" + Style.RESET_ALL)

misc.add_option("--dependencies", 
                action="store_true",
                dest="noncore_dependencies",
                default=False,
                help="Check for third-party (non-core) dependencies.")

misc.add_option("--list-tampers", 
                action="store_true",
                dest="list_tampers",
                default=False,
                help="Display list of available tamper scripts")

misc.add_option("--purge", 
                action="store_true",
                dest="purge",
                default=False,
                help="Safely remove all content from commix data directory.")

misc.add_option("--skip-waf", 
                action="store_true",
                dest="skip_waf",
                default=False,
                help="Skip heuristic detection of WAF/IPS/IDS protection.")

misc.add_option("--mobile", 
                action="store_true",
                dest="mobile",
                default=False,
                help="Imitate smartphone through HTTP User-Agent header.")

misc.add_option("--offline", 
                action="store_true",
                dest="offline",
                default=False,
                help="Work in offline mode.")
# Hidden ZOMIBE and/or experimental options
misc.add_option("--zombie", dest="zombie", action="store_true",
                  help=SUPPRESS_HELP)

misc.add_option("--wizard", 
                action="store_true",
                dest="wizard",
                default=False,
                help="Simple wizard interface for beginner users.")

misc.add_option("--disable-coloring",
                action="store_true",
                dest="disable_coloring",
                default=False,
                help="Disable console output coloring.")

# File system options
filesystem = OptionGroup(parser, "File system access", "These options "
                         "can be used to access the back-end database "
                         "management system underlying file system")


parser.add_option_group(target)
parser.add_option_group(request)
parser.add_option_group(file_access)
parser.add_option_group(modules)
parser.add_option_group(injection)
parser.add_option_group(detection)
parser.add_option_group(misc)
parser.add_option_group(enumeration)
#parser.add_option_group(brute)
#parser.add_option_group(dox)
parser.add_option_group(filesystem)
#parser.add_option_group(windows)
parser.add_option_group(general)


"""
Dirty hack from sqlmap [1], to display longer options without breaking into two lines.
[1] https://github.com/sqlmapproject/sqlmap/blob/fdc8e664dff305aca19acf143c7767b9a7626881/lib/parse/cmdline.py
"""
def _(self, *args):
    _ = parser.formatter._format_option_strings(*args)
    if len(_) > settings.MAX_OPTION_LENGTH:
        _ = ("%%.%ds.." % (settings.MAX_OPTION_LENGTH - parser.formatter.indent_increment)) % _
    return _

parser.formatter._format_option_strings = parser.formatter.format_option_strings
#parser.formatter.format_option_strings = type(parser.formatter.format_option_strings)(_, parser, type(parser))
parser.formatter.format_option_strings = type(parser.formatter.format_option_strings) #(_, parser, type(parser)

#parser.formatter._format_option_strings = parser.formatter.format_option_strings
#parser.formatter.format_option_strings = type(parser.formatter.format_option_strings)(_, parser, type(parser))


#option = parser.get_option("-h")
#options = parser.get_option("-h")
#options.help("Show this help message and exit Show help and exit.")
#(options, args) = parser.parse_args() 

# Dirty hack for making a short option -hh
option = OptionParser("--hh")
option.add_option = ["-hh"]
option.add_option = []
# Dirty hack for inherent help message of switch -h
option = parser.get_option("-h")
option.help = option.help.capitalize().replace("this help", "basic help")

argv = []
prompt = False
#advancedHelp = True
extraHeaders = []

for arg in sys.argv:
  #argv.append(sys.maxunicode(arg, encoding=sys.getfilesystemencoding()))

  

  prompt = "--commi3-shell" in argv

  if prompt:
    parser.usage = ""
    cmdLineOptions.sqlmapShell = True

    _ = ["x", "q", "exit", "quit", "clear"]

    for option in parser.option_list:
      _.extend(option._long_opts)
      _.extend(option._short_opts)

    for group in parser.option_groups:
      for option in group.option_list:
        _.extend(option._long_opts)
        _.extend(option._short_opts)

    autoCompletion(AUTOCOMPLETE_TYPE.SQLMAP, commands=_)

    while True:
      command = None

      try:
        command = input("commi3-shell> ").strip()
        command = sys.maxunicode(command, encoding=sys.stdin.encoding)
      except (KeyboardInterrupt, EOFError):
        print()
        raise SqlmapShellQuitException

      if not command:
        continue
      elif command.lower() == "clear":
        clearHistory()                    
        print ("[i] history cleared")
        saveHistory(AUTOCOMPLETE_TYPE.SQLMAP)
      elif command.lower() in ("x", "q", "exit", "quit"):
        #raise SqlmapShellQuitException
        pass
      elif command[0] != '-':
        print ("[!] invalid option(s) provided")
        print ("[i] proper example: '-u http://www.site.com/vuln.php?id=1 --banner'")
      else:
        saveHistory(AUTOCOMPLETE_TYPE.SQLMAP)
        loadHistory(AUTOCOMPLETE_TYPE.SQLMAP)
        break

    try:
      for arg in shlex.split(command):
        argv.append(sys.maxunicode(arg, encoding=sys.stdin.encoding))
    except ValueError:
      #raise SqlmapSyntaxException
      pass

  # Hide non-basic options in basic help case
  for i in range(len(argv)):
    if argv[i] == "-hh":
      argv[i] = "-h"
    elif argv[i] == "-H":
      if i + 1 < len(argv):
        extraHeaders.append(argv[i + 1])
    elif re.match(r"\A\d+!\Z", argv[i]) and argv[max(0, i - 1)] == "--threads" or re.match(r"\A--threads.+\d+!\Z", argv[i]):
      argv[i] = argv[i][:-1]
      conf.skipThreadCheck = True
    elif argv[i] == "--version":
      print((VERSION_STRING.split('/')[-1]))
      raise SystemExit
    elif argv[i] == "-h":
      advancedHelp = False
      for group in parser.option_groups[:]:
        found = False
        for option in group.option_list:
          if option.dest not in BASIC_HELP_ITEMS:
            option.help = SUPPRESS_HELP
          else:
            found = True
        if not found:
          parser.option_groups.remove(group)

  try:
    (args, _) = parser.parse_args(argv)
  except UnicodeEncodeError as ex:
    print(("\n[!] %s" % ex.object.encode("unicode-escape")))
    raise SystemExit
  except SystemExit:
    if "-h" in argv and not advancedHelp:
      print ("\n[!] to see full list of options run with '-hh'")
    raise

  if extraHeaders:
    if not args.headers:
      args.headers = ""
    delimiter = "\\n" if "\\n" in args.headers else "\n"
    args.headers += delimiter + delimiter.join(extraHeaders)
    
    
    if args.zombie:
      args.url = args.url or ZOMBIE_URL
      
      
      
      if not any((args.data, args.direct, args.url, args.logfile, args.googledork, args.configFile, \
                  args.requestFile, args.updateAll, args.smokeTest, args.liveTest, args.wizard, args.dependencies, \
                  args.purgeOutput, args.pickledOptions, args.sitemapUrl)):
        errMsg = "missing a mandatory option (-d,--d9 -u, -l, -m, -r, -g, -c, -x, --wizard, --update, --purge-output or --dependencies), "
        errMsg += "use -h for basic or -hh for advanced help"
        urllib.error.URLError(errMsg)


#except ValueError as e:
  #parser.error(e)
  
   
  #if not option.version:
    banner()


# Checkall the banner

    
# argv input errors
settings.sys_argv_errors()

"""
The "os_shell" available options.
"""
def os_shell_options():
      print(("""
---[ """ + Style.BRIGHT + Fore.BLUE + """Available options""" + Style.RESET_ALL + """ ]---     
Type '""" + Style.BRIGHT + """?""" + Style.RESET_ALL + """' to get all the available options.
Type '""" + Style.BRIGHT + """back""" + Style.RESET_ALL + """' to move back from the current context.
Type '""" + Style.BRIGHT + """quit""" + Style.RESET_ALL + """' (or use <Ctrl-C>) to quit commix.
Type '""" + Style.BRIGHT + """reverse_tcp""" + Style.RESET_ALL + """' to get a reverse TCP connection.
Type '""" + Style.BRIGHT + """bind_tcp""" + Style.RESET_ALL + """' to set a bind TCP connection.
"""))

"""
The "reverse_tcp" available options.
"""
def reverse_tcp_options():
      print(("""
---[ """ + Style.BRIGHT + Fore.BLUE + """Available options""" + Style.RESET_ALL + """ ]---     
Type '""" + Style.BRIGHT + """?""" + Style.RESET_ALL + """' to get all the available options.
Type '""" + Style.BRIGHT + """set""" + Style.RESET_ALL + """' to set a context-specific variable to a value.
Type '""" + Style.BRIGHT + """back""" + Style.RESET_ALL + """' to move back from the current context.
Type '""" + Style.BRIGHT + """quit""" + Style.RESET_ALL + """' (or use <Ctrl-C>) to quit commix.
Type '""" + Style.BRIGHT + """os_shell""" + Style.RESET_ALL + """' to get into an operating system command shell.
Type '""" + Style.BRIGHT + """bind_tcp""" + Style.RESET_ALL + """' to set a bind TCP connection.
"""))

"""
The "bind_tcp" available options.
"""
def bind_tcp_options():
      print(("""
---[ """ + Style.BRIGHT + Fore.BLUE + """Available options""" + Style.RESET_ALL + """ ]---     
Type '""" + Style.BRIGHT + """?""" + Style.RESET_ALL + """' to get all the available options.
Type '""" + Style.BRIGHT + """set""" + Style.RESET_ALL + """' to set a context-specific variable to a value.
Type '""" + Style.BRIGHT + """back""" + Style.RESET_ALL + """' to move back from the current context.
Type '""" + Style.BRIGHT + """quit""" + Style.RESET_ALL + """' (or use <Ctrl-C>) to quit commix.
Type '""" + Style.BRIGHT + """os_shell""" + Style.RESET_ALL + """' to get into an operating system command shell.
Type '""" + Style.BRIGHT + """reverse_tcp""" + Style.RESET_ALL + """' to get a reverse TCP connection.
"""))

"""
The available mobile user agents.
"""
def mobile_user_agents():

    print(("""---[ """ + Style.BRIGHT + Fore.BLUE + """Available Mobile HTTP User-Agent headers""" + Style.RESET_ALL + """ ]---     
Type '""" + Style.BRIGHT + """1""" + Style.RESET_ALL + """' for BlackBerry 9900 HTTP User-Agent header.
Type '""" + Style.BRIGHT + """2""" + Style.RESET_ALL + """' for Samsung Galaxy S HTTP User-Agent header.
Type '""" + Style.BRIGHT + """3""" + Style.RESET_ALL + """' for HP iPAQ 6365 HTTP User-Agent header.
Type '""" + Style.BRIGHT + """4""" + Style.RESET_ALL + """' for HTC Sensation HTTP User-Agent header.
Type '""" + Style.BRIGHT + """5""" + Style.RESET_ALL + """' for Apple iPhone 4s HTTP User-Agent header.
Type '""" + Style.BRIGHT + """6""" + Style.RESET_ALL + """' for Google Nexus 7 HTTP User-Agent header.
Type '""" + Style.BRIGHT + """7""" + Style.RESET_ALL + """' for Nokia N97 HTTP User-Agent header.
"""))

    while True:
      question_msg = "Which mobile HTTP User-Agent header do you want to use? "
      sys.stdout.write(settings.print_question_msg(question_msg))
      mobile_user_agent = sys.stdin.readline().replace("\n","").lower()
      try:
        if int(mobile_user_agent) in range(0,len(settings.MOBILE_USER_AGENT_LIST)):
          return settings.MOBILE_USER_AGENT_LIST[int(mobile_user_agent)]
        elif mobile_user_agent.lower() == "q":
          raise SystemExit()
        else:
          err_msg = "'" + mobile_user_agent + "' is not a valid answer."  
          print((settings.print_error_msg(err_msg)))
          pass
      except ValueError:
        err_msg = "'" + mobile_user_agent + "' is not a valid answer."  
        print((settings.print_error_msg(err_msg)))
        pass     

"""
The tab compliter (shell options).
"""
def tab_completer(text, state):
    set_options = [option.upper() for option in settings.SET_OPTIONS if option.startswith(text.upper())]
    shell_options = [option for option in settings.SHELL_OPTIONS if option.startswith(text.lower())]
    available_options = shell_options + set_options
    try:
      return available_options[state]
    except IndexError:
      return None

"""
Check if enumeration options are enabled.
"""
def enumeration_options():
  if options.hostname or \
     options.current_user or \
     options.is_root or \
     options.is_admin or \
     options.sys_info or \
     options.users or \
     options.privileges or \
     options.passwords or \
     options.ps_version :
    return True

"""
Check if file access options are enabled.
"""
def file_access_options():
  if options.file_write or \
     options.file_upload or\
     options.file_read:
    return True

# eof
