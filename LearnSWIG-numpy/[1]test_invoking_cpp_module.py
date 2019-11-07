# -*- coding: utf-8 -*-
import numpy as np
import rms

# Functions returning single value
print(rms.rms(np.arange(10)))
print(rms.sum(np.arange(10)))
print(rms.dot(np.arange(5), np.arange(4, -1, -1)))
# Raise exception: shapes NOT match
#print(rms.dot([1, 2, 3, 4], [2, 3]))

# In-place modification
values = np.arange(10).astype(float)
rms.sq_inplace(values)
print(values)

# Functions returning numpy-arrays. 
# The function takes an argument to specify the dimension of output array. 
print(rms.make_array(10))

# Functions taking 2D numpy-arrays
print(rms.sum_mat(np.ones((3, 5))))

# Functions taking and returning 2D numpy-arrays
# SWIG supports only 1D output array 
# See: https://numpy.org/devdocs/reference/swig.interface-file.html#argout-arrays
# So, maybe need more wrapping from the Python side...
m1 = np.arange(8).reshape((2, 4))
m2 = np.arange(20).reshape((4, 5))
print(m1.dot(m2))
print(rms.dot_mat(m1, m2, 10).reshape(2, 5))
# Raise exception: shapes NOT match
#rms.dot_mat(m1, m1.dot(m2), 10)

print(rms.inverse_diff(np.arange(10), 9))

N = 100000
values = np.random.randn(N)
print((rms.inverse_diff(values, N-1) + np.diff(values) == 0).all())

# 50.7 ms ± 880 µs
# %timeit [values[i] - values[i+1] for i in range(N-1)]
# 201 µs ± 29.1 µs
# %timeit (-np.diff(values))
# 356 µs ± 2.17 µs
# %timeit rms.inverse_diff(values, N-1)

