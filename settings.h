#ifdef WIN32
#define util_socket_t intptr_t
#else
#define util_socket_t int
#endif

#define UTIL_SOCKET_ERROR()
#define UTIL_SET_SOCKET_ERROR(errcode)
#define util_socket_geterror(sock)
#define util_socket_error_to_string(errcode)

#define UTIL_AI_PASSIVE     /* ... */
#define UTIL_AI_CANONNAME   /* ... */
#define UTIL_AI_NUMERICHOST /* ... */
#define UTIL_AI_NUMERICSERV /* ... */
#define UTIL_AI_V4MAPPED    /* ... */
#define UTIL_AI_ALL         /* ... */
#define UTIL_AI_ADDRCONFIG  /* ... */

#define util_offsetof(type, field)

struct util_addrinfo {
    int ai_flags;
    int ai_family;
    int ai_socktype;
    int ai_protocol;
    size_t ai_addrlen;
    char *ai_canonname;
    struct sockaddr *ai_addr;
    struct util_addrinfo *ai_next;
};