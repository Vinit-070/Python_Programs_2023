# Write a program to implement basic mathematical operations on using numpy package. 

import numpy as np 
a = np.arange(9, dtype = np.int_).reshape(3,3) 
# a = [[0,1,2],[3,4,5],[6,7,8]] 
print('First array:') 
print(a) 
print('\n') 
print('Second array:') 
b = np.array([10,10,10]) 
print(b) 
print('\n') 
print('Add the two arrays:') 
print(np.add(a,b)) 
print('\n') 
print('Subtract the two arrays:') 
print(np.subtract(a,b)) 
print('\n') 
print('Multiply the two arrays:') 
print(np.multiply(a,b)) 
print('\n') 
print('Divide the two arrays:') 
print(np.divide(a,b))
