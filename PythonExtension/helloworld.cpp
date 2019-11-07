#include <iostream>
#include <Python.h>

using std::system;
using std::cin;
using std::cout;
using std::endl;


int increment_from_py(int a){
    // Import my_py_module
    PyObject *pModule = PyImport_ImportModule("my_py_module");
    if (pModule == nullptr){
        cout << "NULL" << endl;
        return 0;
    }

    // my_py_module.increment
    PyObject *pFunc = PyObject_GetAttrString(pModule, "increment");

    // Build args
    PyObject *pArgs = PyTuple_New(1);
    PyTuple_SetItem(pArgs, 0, PyLong_FromLong(a));

    // Call function
    PyObject *pValue = PyObject_CallObject(pFunc, pArgs);

    int res = PyLong_AsLong(pValue);
    return res;
}


int main()
{
    Py_SetPythonHome(L"D:/Softwares/Anaconda3");

    Py_Initialize();
    PyRun_SimpleString("print(\"Hello Python!\")");
    PyRun_SimpleString("a = 4");
    PyRun_SimpleString("print(a)");
    //PyRun_SimpleString("import sys; sys.path.append(\"D:/Documents/CppFiles/PythonExtension\")");
    
    cout << increment_from_py(400) << endl;

    Py_Finalize();

    system("pause");
    return 0;
}

//cl /o helloworld_cl helloworld.cpp -ID:\Softwares\Anaconda3\include D:\Softwares\Anaconda3\libs\python37.lib
//g++ -o helloworld_gpp helloworld.cpp -ID:\Softwares\Anaconda3\include D:\Softwares\Anaconda3\libs\python37.lib
