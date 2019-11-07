# -*- coding: utf-8 -*-
import numpy as np
cimport numpy as np

np.import_array()

cdef extern from "mean_cy.h":
    double c_mean(double* in_array, int size)

def mean(np.ndarray[double, ndim=1, mode="c"] in_array not None,):
    return c_mean(<double*> np.PyArray_DATA(in_array), in_array.shape[0])
