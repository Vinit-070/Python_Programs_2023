"""
    Author : Vinit Patel
    Aim : Using concept of list comprehension, write a program to transpose m x n matrix.
"""
m = int(input("Enter no. of rows : "))
n = int(input("Enter no. of columns : "))

ans = [[int(input("Enter the values : ")) for i in range(0,m)]for j in range(0,n)]
print("Before Transpose : ",ans)

trans = [[ans[i][j] for i in range(0,n)]for j in range(0,m)]
print("After Transpose : ",trans)