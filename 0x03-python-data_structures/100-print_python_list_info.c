#define PY_SSIZE_T_CLEAN
#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Print info about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, index;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
	}
}
