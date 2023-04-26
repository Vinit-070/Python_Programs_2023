"""
    Author : Vinit Patel
    Aim : Find the list of uncommon elements from two lists using set.
"""
l1 = [1,2,3]
s1 = set(l1)
l2 = [1,12,3]
s2 = set(l2)
p = list(set(s1 ^ s2))
print(p)
