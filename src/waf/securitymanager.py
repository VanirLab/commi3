#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.

For more see the file 'readme/COPYING' for copying permission.


"""

from __future__ import print_function
from concurrent import futures as cf
import socket
import sys, types
import time
import os
import urllib
import io
import logging
import os.path
import hashlib
import shutil
from pathlib import Path, PureWindowsPath, PosixPath, ntpath

 

#PyJava AdminAccessExploit

"""LOad DyNamic Libs --HERE--"""


def read_file(data):
    print("-------------READ_FILE------------------")
    read = os.read(data) #Read files from the users system
    print(("Reading" % read))
    
    return (data)
    
def write_file(data):
    print("-------------WRITE_FILE------------------")
    write = os.write(data)
    print(write)
    return (data)

def delete_file(data, name):
    print("-------------DELETE_FILE------------------")
    delte = os.remove(data)
    deletedir = os.removedirs(name)
    
    return (data, name)

def rename_file(old, new):
    print("-------------RENAME_FILE------------------")
    rename = os.rename()
    os.renames(old, new)
    
    return (old, new)


def create_dir():
    mkdir = os.makedirs()
    
def list_dir():
    print(sorted(os.listdir(sys.argv[1])))
    
    
    
def check_file(file_path, file_name):
    print("-------------FILE_CHECK------------------")
    chfile = os.path.isfile(file_path)
    wfile = ntpath('/../../').root
    if os.path.exists(file_name):
        print("I get the file >Hi dude")
        if not os.path.exists(file_name):
            print(("The File s% it's not created "%file_name))
            os.touch(file_name)
            print(("The file s% has been Created ..."%file_name))        

def obtain_info():
    print("-------------INFO------------------")
    
    class ClassLoader:
        def __init__(self, value):
            self._value = value
            self._version = version
        def getClassLoadingLock(self):
            self._name = __builtins__
        def find_class(self, file):
            file = "../../"
            if file is  True: print("is NULL")
            else: print(" is TRUE")

        
        def def_class(self):
            self._name = name
        def resolv_class(c11):
            try: raise Exception("If c11 is null.")
            except Exception as error:
                print((error))
            
        def find_sys_class(self, name):
            self._name = name
            
            
            
            try: raise Exception('Class could not be found')
            except Exception as error:
                print((error))
                
                return name
            
            
        def def_package(name, self, title, version, vendor, ititle, iversion, ivendor, url):
            print("-------------PACKAGES------------------")
            self._name = name
            self._specTitle = title #private attrib
            self._specVersion = version
            self._specVendor = vendor
            self._implTitle = ititle
            self._implVersion = iversion
            self._implVendor = ivendor
            self._sealBase = urllib.request()
            
            
            
        def get_package(name, self):
            self._name = name
            
            return (name)
        
        def find_lib(self, libname):
            self._libname = libname
            
        def get_sys_class_loader(self, load, data):
            self._load = load
            self._data = data
            
            
            
            

#def security_manager():
def spec_network(new_sock, address):
    print('Connected from', address)
    while True:
        received = new_sock.recv(1024)
        if not received: break
        
        s = received.decode('utf-8', errors='replace')
        print('Recv:', s)
        
        new_sock.sendall(received)
        print('Echo:', s)
        
        new_sock.close()
        print('Disconnected from', address)
        
        
        servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servsock.bind(('localhost', 8881))
        servsock.listen(5)
        servsock.getpeername()
        servsock.getsockname()
        print('Serving at', servsock.getsockname())
        
        with cf.ThreadPoolExecutor(20) as e:
            try:
                while True:
                    new_sock, address = servsock.accept()
                    e.submit(spec_network, new_sock, address)
                    servsock.accept()
            except KeyboardInterrupt:
                pass
            finally:
                servsock.close()
      
    
    
    class Error(Exception):
        """Base class for exceptions in this module."""
        pass
    
    class InputError(Error):
        """Exception raised for errors in the input.
    
        Attributes:
            expr -- input expression in which the error occurred
            msg  -- explanation of the error
        """
        def __init__(self, expr, msg):
            self.expr = expr
            self.msg = msg
    
    class TransitionError(Error):
        """Raised when an operation attempts a state transition that's not
        allowed.
    
        Attributes:
            prev -- state at beginning of transition
            next -- attempted new state
            msg  -- explanation of why the specific transition is not allowed
        """
    
        def __init__(self, prev, next, msg):
            self.prev = prev
            self.next = next
            self.msg = msg        
    
#def create_net_connection():
#def _listen_(): #listen for or accept connections to any port on the users system
#def pop_window(): #Pops a windows without the untrusted window title

def _obtainnames_(): #obtain user,system,home including sys proterties user.name, user.home, user.dir, java.home, java.class.path
    print("-------------SYS------------------")
    homedir = os.environ['HOMEPATH']
    print(homedir)
    appdata = os.environ['LOCALAPPDATA']
    print(appdata)
   # path = os.environ['PATH']
   # print(path)
    compname = os.environ['COMPUTERNAME']
    print(compname)
    windir = os.environ['windir']
    print(windir)
    comspec = os.environ['ComSpec']
    print(comspec)
    cpf = os.environ['CommonProgramFiles']
    print(cpf)
    alup = os.environ['ALLUSERSPROFILE']
    print(alup)
    uprof = os.environ['USERPROFILE']
    print(uprof)
    uname = os.environ['USERNAME']
    print(uname)
    sysroot = os.environ['SystemRoot']
    print(sysroot)
    public = os.environ['PUBLIC']
    print(public)
    #osv = os.environ['OS_VERSION']
    #sockets = os.environ['SOCKETS']
    appdata = os.environ['APPDATA']
    print(appdata)
    #urldir = os.environ['HTTP_DIR']
    temp = os.environ['TMP']
    print(temp)

    
#def sys_props():

def create_log():
    print("-------------LOG------------------")
    path = '../../' #Max with=100
    
    LOG_DIR = os.listdir(path)
    print(LOG_DIR)
    


# Main
if __name__ == '__main__':
    started = time.time()
    #def_package() private attrib DO NOT USE THIS
    _obtainnames_()
    obtain_info()
    create_log()
    
    
    elapsed = time.time() - started
    print("time elapsed: {:.2f}s".format(elapsed))
    
    
    
    

    
    




# eof