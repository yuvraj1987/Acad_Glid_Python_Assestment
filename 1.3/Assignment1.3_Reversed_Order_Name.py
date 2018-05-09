# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:39:18 2018

@author: jkdadhich
"""

# Declare two python Object for User Input First Name and Last Name
# .title() Make First Letter Capital and rest in lower case
# str inbult function used to make every Input as String
User_first_name = str(input(" Enter First Name :\t").title())
User_last_name  = str(input(" Enter Last Name :\t").title())

# CONCATENATE the Fist Name and Last Name with Space
# We Can also add space with User Input as well refer the sample
# sample :- User_first_name = str(input(" Enter First Name :\t").title()+str(" "))

Full_Name =  User_first_name+" "+User_last_name


# Method 1 :-  Using reversed inbult function and result in list and perfrom join

Reversed_Method_1 = "".join(list(reversed(Full_Name)))

# Method 2 :-  Using reversed inbult function and with iterating reverse and perfrom join
Reversed_Method_2 = ''.join(letter for letter in reversed(Full_Name))


# Method 3 :-  Making Reversed for loop with Single Steps in Range and Store Index value and perform join

Reversed_Method_3 = ''.join(Full_Name[i] for i in range(len(Full_Name) - 1, -1, -1))

# Method 4 :-  Most Simple way Slicing

Reversed_Method_4 = Full_Name[::-1]

print ("~*~"*10)
print (" Reversed Out-Put of First Name and Last Name")
print ("~*~"*5)
print (Reversed_Method_1)
print ("~*~"*5)
print (Reversed_Method_2)
print ("~*~"*5)
print (Reversed_Method_3)
print ("~*~"*5)
print (Reversed_Method_4)
print ("~*~"*10)
# You Can do other functionalty with Out-put as few sample Below
print (" Reversed making Tittle of Result :", Reversed_Method_1.title())
print ("~*~"*5)
print (" Reversed making Upper Case of Result :", Reversed_Method_1.upper())
print ("~*~"*5)
print (" Reversed making Lower Case of Result :", Reversed_Method_1.lower())
print ("~*~"*5)
print (" Reversed making Capital Only First Character of Result :", Reversed_Method_1.capitalize())
print ("~*~"*10)






