#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""

import atexit
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from utils import readlineng as readline
__package__ = 'utils'


import logging
import pathlib




class AUTOCOMPLETE_TYPE:
    SQL = 0
    OS = 1
    SQLMAP = 2
    API = 3
class OS:
    LINUX = "Linux"
    MAC = "Mac"
    WINDOWS = "Windows"

try:
    import rlcompleter

    class CompleterNG(rlcompleter.Completer):
        def global_matches(self, text):
            """
            Compute matches when text is a simple name.
            Return a list of all names currently defined in self.namespace
            that match.
            """

            matches = []
            n = len(text)

            for ns in (self.namespace,):
                for word in ns:
                    if word[:n] == text:
                        matches.append(word)

            return matches
except:
    readline._readline = None

def readlineAvailable():
    """
    Check if the readline is available. By default
    it is not in Python default installation on Windows
    """

    return readline._readline is not None

def clearHistory():
    if not readlineAvailable():
        return

    readline.clear_history()

def saveHistory(completion=None):
    try:
        if not readlineAvailable():
            return

        if completion == AUTOCOMPLETE_TYPE.SQL:
            historyPath = pathlib.SQL_SHELL_HISTORY
        elif completion == AUTOCOMPLETE_TYPE.OS:
            historyPath = paths.OS_SHELL_HISTORY
        elif completion == AUTOCOMPLETE_TYPE.API:
            historyPath = paths.API_SHELL_HISTORY
        else:
            historyPath = paths.SQLMAP_SHELL_HISTORY

        try:
            with open(historyPath, "w+"):
                pass
        except:
            pass

        readline.set_history_length(MAX_HISTORY_LENGTH)
        try:
            readline.write_history_file(historyPath)
        except IOError as ex:
            warnMsg = "there was a problem writing the history file '%s' (%s)" % (historyPath, getSafeExString(ex))
            logger.warn(warnMsg)
    except KeyboardInterrupt:
        pass

def loadHistory(completion=None):
    if not readlineAvailable():
        return

    clearHistory()

    if completion == AUTOCOMPLETE_TYPE.SQL:
        historyPath = paths.SQL_SHELL_HISTORY
    elif completion == AUTOCOMPLETE_TYPE.OS:
        historyPath = paths.OS_SHELL_HISTORY
    elif completion == AUTOCOMPLETE_TYPE.API:
        historyPath = paths.API_SHELL_HISTORY
    else:
        historyPath = paths.SQLMAP_SHELL_HISTORY

    if os.path.exists(historyPath):
        try:
            readline.read_history_file(historyPath)
        except IOError as ex:
            warnMsg = "there was a problem loading the history file '%s' (%s)" % (historyPath, getSafeExString(ex))
            logger.warn(warnMsg)

def autoCompletion(completion=None, os=None, commands=None):
    if not readlineAvailable():
        return

    if completion == AUTOCOMPLETE_TYPE.OS:
        if os == OS.WINDOWS:
            # Reference: http://en.wikipedia.org/wiki/List_of_DOS_commands
            completer = CompleterNG({
                "copy": None, "del": None, "dir": None,
                "echo": None, "md": None, "mem": None,
                "move": None, "net": None, "netstat -na": None,
                "ver": None, "xcopy": None, "whoami": None,
            })

        else:
            # Reference: http://en.wikipedia.org/wiki/List_of_Unix_commands
            completer = CompleterNG({
                "cp": None, "rm": None, "ls": None,
                "echo": None, "mkdir": None, "free": None,
                "mv": None, "ifconfig": None, "netstat -natu": None,
                "pwd": None, "uname": None, "id": None,
            })

        readline.set_completer(completer.complete)
        readline.parse_and_bind("tab: complete")

    elif commands:
        completer = CompleterNG(dict(((_, None) for _ in commands)))
        readline.set_completer_delims(' ')
        readline.set_completer(completer.complete)
        readline.parse_and_bind("tab: complete")

    loadHistory(completion)
    atexit.register(saveHistory, completion)