# Write a program to implement basic mathematical operations on using scipy package. 

from scipy import linalg 
import numpy as np 
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]]) 
b = np.array([2, 4, -1]) 
x = linalg.solve(a, b) 
print(x) 
A = np.array([[1,2],[3,4]]) 
#Passing the values to the det function 
x = linalg.det(A) 
#printing the result
print(x) 
l, v = linalg.eig(A) 
#printing the result for eigen values 
print(l) 
#printing the result for eigen vectors 
print(v)
