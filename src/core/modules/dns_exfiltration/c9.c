#include <Python.h>


static PyObject*

c9(PyObject* self)
{
 return Py_BuildValue("s", "Welcome to commi3 security arm!");
}


static char c9_docs[] = "Commi3(): ......\n";

static PyMethodDef c9_funcs[] = {
 {"Commi3", (PyCFunction)c9, METH_NOARGS, c9_docs},
 {NULL}
};

static struct PyModuleDef hello_module = {
 PyModuleDef_HEAD_INIT,
 "commi3",
 c9_docs,
 -1,
 c9_funcs
};

PyMODINIT_FUNC
#if PY_MAJOR_VERSION >= 3
PyInit_c9(void)
{
 return PyModule_Create(&c9_module);
#else
initc9(void)
{
 Py_InitModule3("hello",
 c9_funcs, c9_docs);
#endif
}

