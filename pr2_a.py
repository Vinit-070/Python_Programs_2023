# Author : Vinit Patel
# Aim : Write a program to filter positive numbers from a list.
l = list()
p = list()

n = int(input("Enter Size Of List : "))
for i in range(0, n):
    ele = int(input("Enter the element : "))
    l.append(ele)

for i in l:
    if i > 0:
        p.append(i)
print("After Filtering, our list = ", p)
