# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _mymodule
else:
    import _mymodule

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class int_array(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _mymodule.int_array_swiginit(self, _mymodule.new_int_array(nelements))
    __swig_destroy__ = _mymodule.delete_int_array

    def __getitem__(self, index):
        return _mymodule.int_array___getitem__(self, index)

    def __setitem__(self, index, value):
        return _mymodule.int_array___setitem__(self, index, value)

    def cast(self):
        return _mymodule.int_array_cast(self)

    @staticmethod
    def frompointer(t):
        return _mymodule.int_array_frompointer(t)

# Register int_array in _mymodule:
_mymodule.int_array_swigregister(int_array)

def int_array_frompointer(t):
    return _mymodule.int_array_frompointer(t)

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _mymodule.delete_SwigPyIterator

    def value(self):
        return _mymodule.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _mymodule.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _mymodule.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _mymodule.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _mymodule.SwigPyIterator_equal(self, x)

    def copy(self):
        return _mymodule.SwigPyIterator_copy(self)

    def next(self):
        return _mymodule.SwigPyIterator_next(self)

    def __next__(self):
        return _mymodule.SwigPyIterator___next__(self)

    def previous(self):
        return _mymodule.SwigPyIterator_previous(self)

    def advance(self, n):
        return _mymodule.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _mymodule.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _mymodule.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _mymodule.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _mymodule.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _mymodule.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _mymodule.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _mymodule:
_mymodule.SwigPyIterator_swigregister(SwigPyIterator)

class int_vec(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _mymodule.int_vec_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _mymodule.int_vec___nonzero__(self)

    def __bool__(self):
        return _mymodule.int_vec___bool__(self)

    def __len__(self):
        return _mymodule.int_vec___len__(self)

    def __getslice__(self, i, j):
        return _mymodule.int_vec___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _mymodule.int_vec___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _mymodule.int_vec___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _mymodule.int_vec___delitem__(self, *args)

    def __getitem__(self, *args):
        return _mymodule.int_vec___getitem__(self, *args)

    def __setitem__(self, *args):
        return _mymodule.int_vec___setitem__(self, *args)

    def pop(self):
        return _mymodule.int_vec_pop(self)

    def append(self, x):
        return _mymodule.int_vec_append(self, x)

    def empty(self):
        return _mymodule.int_vec_empty(self)

    def size(self):
        return _mymodule.int_vec_size(self)

    def swap(self, v):
        return _mymodule.int_vec_swap(self, v)

    def begin(self):
        return _mymodule.int_vec_begin(self)

    def end(self):
        return _mymodule.int_vec_end(self)

    def rbegin(self):
        return _mymodule.int_vec_rbegin(self)

    def rend(self):
        return _mymodule.int_vec_rend(self)

    def clear(self):
        return _mymodule.int_vec_clear(self)

    def get_allocator(self):
        return _mymodule.int_vec_get_allocator(self)

    def pop_back(self):
        return _mymodule.int_vec_pop_back(self)

    def erase(self, *args):
        return _mymodule.int_vec_erase(self, *args)

    def __init__(self, *args):
        _mymodule.int_vec_swiginit(self, _mymodule.new_int_vec(*args))

    def push_back(self, x):
        return _mymodule.int_vec_push_back(self, x)

    def front(self):
        return _mymodule.int_vec_front(self)

    def back(self):
        return _mymodule.int_vec_back(self)

    def assign(self, n, x):
        return _mymodule.int_vec_assign(self, n, x)

    def resize(self, *args):
        return _mymodule.int_vec_resize(self, *args)

    def insert(self, *args):
        return _mymodule.int_vec_insert(self, *args)

    def reserve(self, n):
        return _mymodule.int_vec_reserve(self, n)

    def capacity(self):
        return _mymodule.int_vec_capacity(self)
    __swig_destroy__ = _mymodule.delete_int_vec

# Register int_vec in _mymodule:
_mymodule.int_vec_swigregister(int_vec)

class double_vec(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _mymodule.double_vec_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _mymodule.double_vec___nonzero__(self)

    def __bool__(self):
        return _mymodule.double_vec___bool__(self)

    def __len__(self):
        return _mymodule.double_vec___len__(self)

    def __getslice__(self, i, j):
        return _mymodule.double_vec___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _mymodule.double_vec___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _mymodule.double_vec___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _mymodule.double_vec___delitem__(self, *args)

    def __getitem__(self, *args):
        return _mymodule.double_vec___getitem__(self, *args)

    def __setitem__(self, *args):
        return _mymodule.double_vec___setitem__(self, *args)

    def pop(self):
        return _mymodule.double_vec_pop(self)

    def append(self, x):
        return _mymodule.double_vec_append(self, x)

    def empty(self):
        return _mymodule.double_vec_empty(self)

    def size(self):
        return _mymodule.double_vec_size(self)

    def swap(self, v):
        return _mymodule.double_vec_swap(self, v)

    def begin(self):
        return _mymodule.double_vec_begin(self)

    def end(self):
        return _mymodule.double_vec_end(self)

    def rbegin(self):
        return _mymodule.double_vec_rbegin(self)

    def rend(self):
        return _mymodule.double_vec_rend(self)

    def clear(self):
        return _mymodule.double_vec_clear(self)

    def get_allocator(self):
        return _mymodule.double_vec_get_allocator(self)

    def pop_back(self):
        return _mymodule.double_vec_pop_back(self)

    def erase(self, *args):
        return _mymodule.double_vec_erase(self, *args)

    def __init__(self, *args):
        _mymodule.double_vec_swiginit(self, _mymodule.new_double_vec(*args))

    def push_back(self, x):
        return _mymodule.double_vec_push_back(self, x)

    def front(self):
        return _mymodule.double_vec_front(self)

    def back(self):
        return _mymodule.double_vec_back(self)

    def assign(self, n, x):
        return _mymodule.double_vec_assign(self, n, x)

    def resize(self, *args):
        return _mymodule.double_vec_resize(self, *args)

    def insert(self, *args):
        return _mymodule.double_vec_insert(self, *args)

    def reserve(self, n):
        return _mymodule.double_vec_reserve(self, n)

    def capacity(self):
        return _mymodule.double_vec_capacity(self)
    __swig_destroy__ = _mymodule.delete_double_vec

# Register double_vec in _mymodule:
_mymodule.double_vec_swigregister(double_vec)


def throw_exception():
    return _mymodule.throw_exception()

def average(v):
    return _mymodule.average(v)

def half(v):
    return _mymodule.half(v)

def half_in_place(v):
    return _mymodule.half_in_place(v)

def double_str(s):
    return _mymodule.double_str(s)

def half_str(s):
    return _mymodule.half_str(s)

def sum_array(arr, n):
    return _mymodule.sum_array(arr, n)

def add(x, y):
    return _mymodule.add(x, y)

def sub(x, y):
    return _mymodule.sub(x, y)

def negate(z):
    return _mymodule.negate(z)

def next_fab(a1, a2):
    return _mymodule.next_fab(a1, a2)

def fact(n):
    return _mymodule.fact(n)

def my_mod(n, m):
    return _mymodule.my_mod(n, m)
class Wall(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _mymodule.Wall_swiginit(self, _mymodule.new_Wall(*args))

    def setWall(self, _s):
        return _mymodule.Wall_setWall(self, _s)

    def getWall(self):
        return _mymodule.Wall_getWall(self)
    x = property(_mymodule.Wall_x_get, _mymodule.Wall_x_set)
    __swig_destroy__ = _mymodule.delete_Wall

# Register Wall in _mymodule:
_mymodule.Wall_swigregister(Wall)
cvar = _mymodule.cvar



