#include <python.h>
#include <object.h>
#include <listobjects.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListobject *_obj = (pyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated %li\n", obj->allocate);
	i = 0;
	while (i < size)
	{
		printf("Element %i: %s\n", i, py_TYPE (_obj->item[i]));
		i++;
	}
}
