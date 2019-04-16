#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.

For more see the file 'readme/COPYING' for copying permission.
"""
"""Settings for DNS"""


import os
import sys





#Time for DNS

EAI_NODATA = 1
MAX_TIMEOUT = 3 # Default is 3
MAX_INFLIGHT = 64
RANDOM_CASE = 1
BIND_TO_ADDRESS = "0.0.0.0"
ALLOW_SKEW = 3 

#Standard integer types in Commi3
uint64_t = int(64) #Not signed
int64_t = int(64) #Signed
uint32_t = int(32) #Not signed
int32_t = int(32) #Signed
uint16_t = int(16) #Not signed
int16_t = int(16) # Signed
uint8_t = int(8) #Not signed
int8_t = int(8) #Signed

#ERRORS FOR DNS

DNS_ERR_NONE = b'No error occurred'

#Creating and configuring an dns_base change in comm3.conf
#WINDOWS usage:
#[NOTICE] Windows doesnt have a comm3.conf file use the dns_base_config_windows_nameservers() function
DNS_OPTION_SEARCH = sys.argv[0]
DNS_OPTION_NAMESERVERS = sys.argv[0]
DNS_OPTION_MISC = sys.argv[0]
DNS_OPTION_HOSTSFILE = sys.argv[0]
DNS_OPTIONS_ALL = sys.argv[0]

#__DNS__ lookup
DNS_ANSWER_SECTION = 0
DNS_AUTHORITY_SECTION = 1
DNS_ADDITIONAL_SECTION = 2
DNS_TYPE_A = 1
DNS_TYPE_NS = 2
DNS_TYPE_CNAME = 5
DNS_TYPE_SOA = 6
DNS_TYPE_PTR = 12
DNS_TYPE_MX = 15
DNS_TYPE_TXT = 16
DNS_TYPE_AAAA = 28
#DNS priority
class DNS_PRIORITY:
    LOWEST = -100
    LOWER = -50
    LOW = -10
    NORMAL = 0
    HIGH = 10
    HIGHER = 50
    HIGHEST = 100

  #Portable blocking name resolution  
class UTIL_ADDRINFO(object):
    def __init__(self):
        self.ai_flags
        self.ai_family = int
        self.ai_socktype = int 
        self.ai_protocol = int
        self.ai_addrlen = size_t
        self.ai_canonname = str
        self.sockaddr_ai_addr = str
        self.evutil_addrinfo_ai_next = str
        
#DNS request       
class DNS_REQ_SERVER(object):
    def __init__(self):
        self.flags
        self.nquestions
        self.dns_server_question = str

class DNS_QUEST_SERVER(object):
    def __init__(self):
        self.type = int
        self.dns_question_class = int
        self.name[1] = str

#Current DNS  functions
class GLOBAL_DNS(object):
    def __init__(self):
        event_base_new()
        dns_base_free()
        dns_base_nameserver_add()
        dns_base_count_nameservers()
        dns_clear_nameservers_and_suspend()
        dns_base_nameserver_ip_add()
        dns_base_resolve_ipv4()
        dns_base_resolve_ipv6()
        dns_base_resolve_reverse()
        dns_base_resolve_reverse_ipv6()
        dns_base_set_option()
        dns_base_resolv_conf_parse()
        dns_base_search_clear()
        dns_base_search_clear()
        dns_base_config_windows_nameservers()
