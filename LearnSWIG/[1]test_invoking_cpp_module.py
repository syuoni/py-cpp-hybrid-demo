# -*- coding: utf-8 -*-
import mymodule

# Global variables
print(mymodule.cvar.my_variable)

# Functions
print(mymodule.fact(6))
print(mymodule.my_mod(6, 4))

# Classes
w = mymodule.Wall(5)
print(w.getWall())
w.setWall(10)
print(w.getWall())
# Do not know how to construct int * type in Python...
print(w.x)

# In-place inputs & outputs
print(mymodule.add(3, 4))
print(mymodule.sub(3, 4))
print(mymodule.negate(5))
print(mymodule.next_fab(*mymodule.next_fab(3, 4)))

# C-arrays
a = mymodule.int_array(500)
for i in range(500):
    a[i] = i
print(a[300])
print(mymodule.sum_array(a, 500))

# C-strings
print(mymodule.half_str("aaabbbbccc"))

# C++ std::string
print(mymodule.double_str("abc"))

# C++ std::vector
iv = mymodule.int_vec(10)
dv = mymodule.double_vec(10)
for i in range(10):
    iv[i] = i**2
    dv[i] = i**2

print(mymodule.average(iv))
print(mymodule.average([1, 3, 4, 10]))

print(mymodule.half([1, 2, 4, 10]))

# Raise exception, cannot modify in-place
#print(mymodule.half_in_place([1, 2, 4, 10]))

mymodule.half_in_place(dv)
for i in range(10):
    print(dv[i])

# Exceptions
mymodule.throw_exception()


