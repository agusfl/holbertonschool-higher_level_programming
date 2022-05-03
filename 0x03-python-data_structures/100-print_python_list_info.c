#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: somthing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, index;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	index = 0;
	while (index < size)
	{
		printf("Element %ld: %s\n",
		       index,
		       (PY_TYPE(PyList_GetItem(p, index)))->tp_name);
		index++;
	}
}
