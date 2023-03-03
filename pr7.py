# Author : Vinit Patel
# Using concept of regular expressions (re), Write a program to check the validity of password input by
# users. Following are the criteria for checking the password :
# i. At least 1 letter between [a-z]
# ii. At least 1 number between [0-9]
# iii. At least 1 letter between [A-Z]
# iv. At least 1 special character
# v. Min. length of transaction password: 6
# vi. Max. length of transaction password: 12
import re
S = input("Enter Password : ")
if re.search('[a-z]', S):
    if re.search('[A-Z]', S):
        if re.search('[0-9]', S):
            if re.search('[@#$%&]', S):
                if len(S) > 6 and len(S) < 12:
                    print("Password is Valid !!!")
                else:
                    print("Password is too Short !!")
            else:
                print("Special Character is Missing !!")
        else:
            print("No numeric value present !!")
    else:
        print("Uppercase value missing")
else:
    print("No lowercase value present")
