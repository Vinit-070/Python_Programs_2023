# Author : Vinit Patel
# Aim : Write a program to check whether a passed letter is a vowel or not.
letter = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
alpha = input("Enter the letter : ")
if alpha in letter:
    print(alpha, " is a vowel")
else:
    print(alpha, " is not a vowel")
