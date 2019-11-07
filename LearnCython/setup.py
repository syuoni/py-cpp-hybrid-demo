# -*- coding: utf-8 -*-
from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("mean_cy", sources=["mean_cy.pyx", "source.c"], include_dirs=[numpy.get_include()])],
)

