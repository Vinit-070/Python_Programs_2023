# Author : Vinit Patel
# Aim : Write a program to get the maximum and minimum value from a dictionary.
d = {}
n = int(input("Enter Size of Dictionary : "))
for i in range(n):
    k = input("Enter the Key : ")
    v = int(input("Enter the Value : "))
    d.update({k: v})
print(d)
val = (list(d.values()))

max = val[0]
for i in val:
    if max < i:
        max = i
print("Maximum value = ", max)
min = val[0]
for i in val:
    if min > i:
        min = i
print("Minimum value = ", min)
