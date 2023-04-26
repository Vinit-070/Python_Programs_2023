
"""
 Author : Vinit Patel
 Aim : Using concept of list comprehension, write a program to print the
    Fibonacci sequence in comma separated form with a given 'n' input by console.
"""

def f(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return (f(x-1)+f(x-2))
n = int(input("Enter the number : "))
ans = [str(f(x))for x in range(0,n+1)]
print(",".join(ans))


