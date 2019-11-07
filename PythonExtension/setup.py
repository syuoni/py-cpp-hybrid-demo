# -*- coding: utf-8 -*-
from setuptools import setup, Extension
#from distutils.core import setup, Extension

my_cpp_module = Extension("my_cpp_module", sources=["my_cpp_module.cpp"])
setup(ext_modules=[my_cpp_module])

# python setup.py build
# error: Microsoft Visual C++ 14.0 is required. 
# Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
