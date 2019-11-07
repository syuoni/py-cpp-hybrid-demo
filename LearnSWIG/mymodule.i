/* File: mymodule.i */
%module mymodule

%{
#include "my_cpp_functions.h"
%}

%include "carrays.i"
%array_class(int, int_array);

%include "typemaps.i"

// The directives later invalidate the former directives, if 
// they use the same variable names.
%apply int *OUTPUT {int *res};
%apply int *INPUT {int *x, int *y};
%apply int *INOUT {int *z, int *a1, int *a2};
%apply (char *STRING, int LENGTH) {(char *s, int n)};

%include "std_string.i"
%include "std_vector.i"
namespace std {
    %template(int_vec) vector<int>;
    %template(double_vec) vector<double>;
}

%include "exception.i"
%exception throw_exception {
    try {
        $action
    } catch (runtime_error &e) {
        SWIG_exception(SWIG_RuntimeError, const_cast<char*>(e.what()));
    }
}


%include "my_cpp_functions.h"

/*
swig -c++ -python mymodule.i

// Both directives work
cl /LD mymodule_wrap.cxx my_cpp_functions.cpp /o _mymodule.pyd -ID:\Softwares\Anaconda3\include D:\Softwares\Anaconda3\libs\python37.lib
g++ -fPIC -shared mymodule_wrap.cxx my_cpp_functions.cpp -o _mymodule.pyd -ID:\Softwares\Anaconda3\include D:\Softwares\Anaconda3\libs\python37.lib
*/