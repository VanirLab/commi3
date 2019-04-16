#include <python.h>
#include "settings.h"


static PyObject*


static struct PyModuleDef module = {
 PyModuleDef_HEAD_INIT,
 util_addrinfo,
 -1,
 util_socket_t
};


PyMODINIT_FUNC
get_tcp_socket_for_host(void)
{
    char port_buf[6];
    struct util_addrinfo hints;
    struct util_addrinfo *answer = NULL;
    int err;
    util_socket_t sock;
    
    
  
    return(&module);
}


