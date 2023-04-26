# Write a program to count frequency of elements and storing in dictionary using zip().

s=input("enter any string: ")
l=s.split()
print(l)
n=[l.count(i) for i in l]
d=dict(zip(l,n))
print(d)
