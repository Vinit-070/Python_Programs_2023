# Author : Vinit Patel
# Aim : Write a program to find factorial of a number.
n = int(input("Enter the Number : "))
def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)

if n < 0:
    print("Invalid Number !!")
else:
    ans = fact(n)
    print("Factorial of ", n, " is ", ans)

''' -->> Another way by using intrusion <<--
fact=1
for i in range(1,n+1):
    fact = fact*i
print("Factorial of ",n," is ",fact)
'''
