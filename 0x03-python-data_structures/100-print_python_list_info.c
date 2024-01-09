#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListobject *_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated %li\n", obj->allocated);
	i = 0;
	while (i < size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(_obj->ob_item[i]->tp_name));
		i++;
	}
}
