# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:35:06 2024

@author: marku
"""

"""
Repeat all the examples
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# How to check the version of the numpy package
# print('numpy:', np.__version__)
# print(dir(np)) # Checking the available methods

python_list = [1,2,3,4,5]
numpy_array_from_list = np.array(python_list) 
numy_array_from_list2 = np.array(python_list, dtype= float)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
# print(type (numpy_two_dimensional_list))
# print(numpy_two_dimensional_list)

print('shape of nums: ', two_dimensional_list.shape) # print the shape of array

#%% 
# math operators
vec1 = np.array([1,2,3,4,5])
matrix1 = np.array([[0,1,2], [3,4,5], [6,7,8]]) # not actually a matrix!!!

print(vec1 + 5) # Addition
print(matrix1 - 5) # Substraction
print(matrix1 * 5) # Multiplication
print(vec1 / 5) # Divition
print(vec1 % 3) # Modulus (find remainder)
print(vec1 // 3) # Floor Division (division without remainder)
print(vec1 ** 3) # exponential


#%%
# Check data types
#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool') # only false if 0
x = np.array([1,2,3], dtype=np.complex128) # complex number array

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
# Length of one array element in bytes.
print(x.itemsize)

#%%
# Indexing & slicing
print('First row: \n', matrix1[0])
print('Second row: \n', matrix1[1])
print('Third row: \n', matrix1[2])

print('First column: \n', matrix1[:,0])
print('Second column: \n', matrix1[:,1])
print('Third column: \n', matrix1[:,2])

print('Top left part of matrix:\n', matrix1[0:2,0:2]) #first index is included, second one not
print('The reveresed matrix: \n', matrix1[::-1,::-1]) # revereses rows and columns

#%% 
numpy_zeroes = np.zeros((3,3),dtype=int,order='C') # matrix only 0
numpy_ones = np.ones((3,3),dtype=int,order='C') # matrix only 1
twoes = numpy_ones * 2 # matrix only 2

#%%
# Reshape
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
flattened = reshaped.flatten() # makes a vector out of a matrix
print(flattened) 

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two))) # Horitzontal Stack
print('Vertical Append: \n', np.vstack((np_list_one, np_list_two))) # Vertical Stack

#%%
random_floats = np.random.random(5) # Generate 5 random number between 0 and 1
random_int  = np.random.randint(0, 11) # Generate 1 random int between 0 and 10
random_int_matr = np.random.randint(2,10, size=(3,3))  # Generating a random integers between 0 and 10

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 200) # Generate random normal distribution 
sns.set()
plt.hist(normal_array, color="grey", bins=50)

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10)) # Randomly choose between given choices

#%%
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float)) #Define a 4x4 matrix
np.asarray(four_by_four_matrix)[2] = 2 # convert the input as array
four_by_four_matrix[3] = 3 # this works the same as above?!

#%% 
# numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1) # Create an array of values between 0 and 19
np.linspace(1.0, 5.0, num=10) # Create an array with 10 entries of linear distance between 1 and 5
np.linspace(1.0, 5.0, num=5, endpoint=False) # not include the last value
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
np.logspace(2, 4.0, num=4)

#%% 
# included statistical functions 
np_normal_dis = np.random.normal(5, 0.5, 100)

## min, max, mean, median, sd
print('min: ', np_normal_dis.min()) # or np.min()
print('max: ', np_normal_dis.max()) # or np.max()
print('mean: ',np_normal_dis.mean()) # or np.mean()
print('median: ', np.median(np_normal_dis)) # or np.median()
print('sd: ', np_normal_dis.std()) # or np.std()
print('mode: ', stats.mode(np_normal_dis)) # mode is the most common number

print('=== Column ==')
print('Column with minimum: ', np.amin(matrix1,axis=0)) #amin = min along axis
print('Column with maximum: ', np.amax(matrix1,axis=0)) #amax = max along axis
print('=== Row ==')
print('Row with minimum: ', np.amin(matrix1,axis=1))
print('Row with maximum: ', np.amax(matrix1,axis=1))

#%%
# Repeating sequence
a = [1,2,3]

print('Tile:   ', np.tile(a, 2)) # Repeat whole of 'a' 2x 
print('Repeat: ', np.repeat(a, 2)) # Repeat each element of 'a' 2x

#%%
# Linear algebra
f = np.array([1,2,3]) 
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23; Dot product: product of two arrays

h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i) ### Matmul: matruc product of two arrays

## Determinant 2*2 matrix
### 5*8-7*6
np.linalg.det(i)

#%%
# Gaussian normal distribution

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()