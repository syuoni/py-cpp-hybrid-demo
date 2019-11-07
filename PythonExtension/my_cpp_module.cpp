#include <iostream>
#include <Python.h>

using std::cin;
using std::cout;
using std::endl;

int increment(int a){
    return a + 1;
}

static PyObject *_increment(PyObject *self, PyObject *args){
    int _a, res;

    if (!PyArg_ParseTuple(args, "i", &_a)){
        return NULL;
    }
    res = increment(_a);
    return PyLong_FromLong(res);
}

int pow(int a, int n){
    int res = 1;
    int base = a;
    while (n > 0){
        if (n % 2 == 1){
            res *= base;
        }
        base *= base;
        n /= 2;
    }
    return res;
}

static PyObject *_pow(PyObject *self, PyObject *args){
    int _a, _n, res;

    if (!PyArg_ParseTuple(args, "ii", &_a, &_n)){
        return NULL;
    }
    res = pow(_a, _n);
    return PyLong_FromLong(res);
}

static PyMethodDef MyCppModuleMethods[] = {
    {"increment", _increment, METH_VARARGS, ""}, 
    {"pow", _pow, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef my_cpp_module = {
    PyModuleDef_HEAD_INIT, "my_cpp_module", NULL, -1, MyCppModuleMethods
};

PyMODINIT_FUNC PyInit_my_cpp_module(void){
    PyObject *m = PyModule_Create(&my_cpp_module);
    if (m == NULL){
        return NULL;
    }else{
        cout << "Init my_cpp_module" << endl;
        return m;
    }
}

// cl /LD my_cpp_module.cpp /o my_cpp_module.pyd -ID:\Softwares\Anaconda3\include D:\Softwares\Anaconda3\libs\python37.lib
// g++ -fPIC -shared my_cpp_module.cpp -o my_cpp_module.pyd -ID:\Softwares\Anaconda3\include D:\Softwares\Anaconda3\libs\python37.lib
