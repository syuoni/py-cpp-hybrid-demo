# -*- coding: utf-8 -*-
import numpy as np
cimport numpy as np

np.import_array()

cdef extern from "mean_cy.h":
    double c_mean(double* in_array, int size)

def mean(np.ndarray[double, ndim=1, mode="c"] in_array not None,):
    return c_mean(<double*> np.PyArray_DATA(in_array), in_array.shape[0])


# Since the Cython is dependent on the Python installed, the 
# mingw cannot be used to compile the resulting mean_cy.c file.
# cython mean_cy.pyx -o mean_cy.c
# g++ -fPIC -shared mean_cy.c source.c -o mean_cy.pyd -ID:\Softwares\Anaconda3\include -ID:\Softwares\Anaconda3\Lib\site-packages\numpy\core\include D:\Softwares\Anaconda3\libs\python37.lib
# cl /LD mean_cy.c source.c /o mean_cy.pyd -ID:\Softwares\Anaconda3\include -ID:\Softwares\Anaconda3\Lib\site-packages\numpy\core\include D:\Softwares\Anaconda3\libs\python37.lib

# python setup.py build_ext --inplace
