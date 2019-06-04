import numpy as np

#_________________________________________________________________________________________________________________
# First part: Numpy arrays

print('\nFirst part: Numpy arrays\n')

lst = [1, 2, 3, 4]

np_arr = np.array(lst)
print(np_arr, '\n')

# 2Dimensional array
np_arr_2d = np.array([lst, lst])
print(np_arr_2d, '\n')

np_arr_2d_man = np.array([[2,4,6],[2,7,9], [3,1,1]])
print(np_arr_2d_man, '\n')

# Crate matrix , with zeros and main diagonal with 1 in argument we write size of matrix
print(np.eye(4), '\n')
# If you multiply your np.eye function, you multiply each element of matrix
print(10 * np.eye(4), '\n')
# Matrix where each element is 0, in shape you must enter rows and colums of matrix
print(np.zeros(shape=(4,6)), '\n')
# The same as np.zeros but with ONES
print(np.ones(shape=(3, 3)), '\n')

# Generate 10 elements array, where element from 0 to 9 from low to hight
print(np.arange(10), '\n')
# Generate array from -5 to 9
print(np.arange(-5, 10), '\n')
# Generate array from -5 to 9 with step 3
print(np.arange(-5, 10, 3), '\n')
# Also we can decrease value with negative step
print(np.arange(40, 10, -3), '\n')

# Similar as np.arange, but devide numbers in other way
print(np.linspace(0, 20, 5), '\n')

# Random array generator, first parameter is number of arrays, second count elements in this arrays
print(np.random.rand(3, 3), '\n')
# 2 times y've generated Matrix(3 x 6)
print(np.random.rand(2, 3, 6), '\n')

# Also random generator
print(np.random.randn(4, 5), '\n')

# Array generator with  n <= element <= m third parameter is elements count in array
print(np.random.randint(10, 50, 5))

# Some operations with array

mat = np.random.randn(4, 5)
print(type(mat))
# Size of array
print(mat.size)
# Matrix dimension
print(mat.shape)
# Can work only if your array count and element count can accommodate
print(mat.reshape(2, 10))
# Type of elements in array
print(mat.dtype)


#_________________________________________________________________________________________________________________
# Second Part: Indexing and functions
print('\n Second Part: Indexing and functions \n')
arr = np.arange(50, 70)
print(arr)
# Compare each element of array with 55 and return True/False
print(arr > 55)
# Count of elements that are greater then 55
print(sum(arr > 55))
# Add some number to each element of array also you can do it with every math operation such as: +-*/,cos,sin,tan...
print(arr + 100)
# Sum of all values in array
print(np.sum(arr))
# Average value in array
print(np.mean(arr))

matr = np.random.rand(5, 5)
print(matr)
# Slices works the same
print(matr[1 : 3, :2])


#_________________________________________________________________________________________________________________
# Third Part: Some more functions

print('\nThird Part: Some more functions\n')

arr_1 = np.random.random(size=(3, 3))
arr_2 = np.random.random(size=(3, 3))

print(arr_1, '\n')
print(arr_2, '\n')

# Combine matrices rows, first elements of arr_1 in row then elements of arr_2
print(np.hstack((arr_1, arr_2)), '\n')
# Combine matrices columns, first columns of arr_1 in row then columns of arr_2
print(np.vstack((arr_1, arr_2)), '\n')


arr_1 = 10 * arr_1

# Rounding numbers down
print(np.floor(arr_1), '\n')
# Rounding numbers up
print(np.ceil(arr_1), '\n')

new_matr = np.ceil(arr_1)

# Calculate summ of each column
print(np.sum(new_matr, axis=0))
# Calculate summ of each row you can use it with: mean,
print(np.sum(new_matr, axis=0))

# Find unique values
print(np.unique(new_matr))

#_________________________________________________________________________________________________________________
# Fourths part: Linear algebra functions Numpy

print('\nFourths part: Linear algebra functions Numpy\n')

matr = np.array([[1, 2], [3, 4]])
matr1 = np.array([[1, 2], [3, 4]])

# Find matrix determinator
print(np.linalg.det(matr), '\n')
# Inverse matrix
print(np.linalg.inv(matr), '\n')
# Swap elements on main diagonal
print(matr.transpose(), '\n')
# Summ elements on main diagonal
print(matr.transpose(), '\n')
# All math operation with elements of matrices
print(matr * matr1, '\n')
# True matrix elements mult
print(matr.dot(matr1), '\n')

# Solve systems of equations like: 2x + y = 1 and x + y = 2

# Array of coefficients
M0 = np.array([[2, 1], [1, 1]])
# Array of values
M1 = np.array([1, 2])
# Function that solve our equation
print(np.linalg.solve(M0, M1), '\n')

#_________________________________________________________________________________________________________________
# Fives part: List vs Numpy Array

print('\nFives part: List vs Numpy Array\n')

# In list you can keep all type of elements in one array
a = [1, 2, 3, 1.2, 'sdfas', True]
# In np.array this values would be converted into strings
print(np.array(a), '\n')

# Numpy arrays and functions are very hight performance
# When you store numpy array in the memory it stores like array in other languages
# When you resize your np.array, it destroys old array and create new resized

#_________________________________________________________________________________________________________________
# Sixth part: Views vs Copy

print('\nSixth part: Views vs Copy\n')

a = np.array([2, 5, 0, 10])
# Copy all elements from array a to c, elements depends on each other
b = a.view()
b[0] = -100
# Elements have changed in array a and array b
print(a ,'\n', b)
# Copy all elements from array a to c, elements do not depend on each other
c = a.copy()
c[1] = -500
# Element have changed only in array c
print(a , '\n', b, '\n', c)

#_________________________________________________________________________________________________________________
# Seventh part: Split, concatenate, tile and repeat

print('\nSeventh part: Split, concatenate, tile and repeat\n')

# We've created array of 6 elements and reshape him into 4 arrays each consist of 6 element
a = np.arange(24).reshape(4, 6)
b = np.arange(100, 124).reshape(4, 6)
print(a, '\n')

# We can split our array into more arrays
print(np.split(a, 2), '\n')
# Split by columns
print(np.split(a, 2, axis=1), '\n')

# Concatenation of a and b
print(np.concatenate((a, b)), '\n')

a = np.arange(5)
b = np.arange(8).reshape(2, 4)

# We can replicate array N times
print(np.tile(a, 3), '\n')
# We can do it with N dimensional arrays
print(np.tile(b, 3), '\n')
print(np.tile(b, (2, 1)), '\n')
print(np.tile(b, (2, 2)), '\n')
print(np.tile(b, (5, 3)), '\n')

# We can repeat every single element in array N times
print(np.repeat(a, 2), '\n')
print(np.repeat(b, 2), '\n')
print(np.repeat(b, 2, axis=0), '\n')
print(np.repeat(b, 5, axis=0), '\n')
print(np.repeat(b, 5, axis=1), '\n')


