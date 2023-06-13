#include <listobject.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - function prints some basic info about Python lists.
 * @p: pointer to the corresponding type object
 * Return:void
 */
void print_python_list_info(PyObject *p)
{
	int counter = 0;
	PyListObject *object = (PyListObject *)p
	long int length = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", object->allocated);
	for (counter; counter < length; counter++)
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[counter])->tp_name);
}
