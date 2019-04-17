#!/usr/bin/env python3
# encoding: UTF-8


"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.


For more see the file 'readme/COPYING' for copying permission.
"""

import re



# Reference: http://www.w3.org/Protocols/HTTP/Object_Headers.html#uri
URI_HTTP_HEADER = "URI"
WAF_ATTACK_VECTOR = (
                        "",  # NIL
                        "search=<script>alert(1)</script>",
                        "file=../../../../etc/passwd",
                        "q=<invalid>foobar",
                        "id=1 %s" % IDS_WAF_CHECK_PAYLOAD
                     )

__product__ = "UrlScan (Microsoft)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTOR:
        page, headers, code = get_page(get=vector)
        retval = re.search(r"Rejected-By-UrlScan", headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None
        if retval:
            break

    return retval