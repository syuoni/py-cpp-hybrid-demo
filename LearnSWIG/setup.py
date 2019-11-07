from distutils.core import setup, Extension


m = Extension('_mymodule', sources=['mymodule_wrap.cxx', 'my_cpp_functions.cpp'])

setup (name = '_mymodule',
       version = '0.1',
       author      = "syuoni",
       description = """Testing SWIG""",
       ext_modules = [m],
       py_modules = ["_mymodule"])

# Only work when using MSVC 
# python setup.py build_ext --inplace