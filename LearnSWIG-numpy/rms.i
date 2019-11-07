%module rms

%{
#define SWIG_FILE_WITH_INIT
#include "rms.h"
%}

%include "numpy.i"

%init %{
import_array();
%}

// "%apply" and "%exception" directives should be put before the declaration of functions
%apply (double *IN_ARRAY1, int DIM1) {(double *seq, int n)};
%apply (double *IN_ARRAY1, int DIM1) {(double *seq, int m)};
%apply (double *IN_ARRAY1, int DIM1) {(double *seq1, int n1), (double *seq2, int n2)};

%apply (double *INPLACE_ARRAY1, int DIM1) {(double *ipseq, int n)};
%apply (double *ARGOUT_ARRAY1, int DIM1) {(double *outseq, int n), 
                                          (double *outseq, int m),
                                          (double *mat3, int nm3)};

%apply (double *IN_ARRAY2, int DIM1, int DIM2) {(double *mat, int n, int m), 
                                                (double *mat1, int n1, int m1), 
                                                (double *mat2, int n2, int m2)};

%include "exception.i"
%exception {
    try {
        $action
    } catch (std::runtime_error &e) {
        SWIG_exception(SWIG_RuntimeError, const_cast<char*>(e.what()));
        // PyErr_SetString(PyExc_Exception, const_cast<char*>(e.what()));
        // SWIG_fail;
    }
}

%include "rms.h"

/*
swig -c++ -python rms.i
cl /LD rms_wrap.cxx rms.cpp /o _rms.pyd -ID:\Softwares\Anaconda3\include -ID:\Softwares\Anaconda3\Lib\site-packages\numpy\core\include D:\Softwares\Anaconda3\libs\python37.lib
g++ -fPIC -shared rms_wrap.cxx rms.cpp -o _rms.pyd -ID:\Softwares\Anaconda3\include -ID:\Softwares\Anaconda3\Lib\site-packages\numpy\core\include D:\Softwares\Anaconda3\libs\python37.lib 
*/