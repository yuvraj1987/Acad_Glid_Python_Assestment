# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:26:39 2018

@author: jkdadhich
"""

# Input for User Inter-face,  entering the Value with Comma as seperator
print ("~*~"*10)
User_Input = input(" Enter Values Using Comma Seprated :\t")
print ()

Result_ =  User_Input.split(",") # Using Split Function Will remove "," Commas

"""NOTE :- Once you Split String It's Automatically Convert String to List
           Have look over below Sample """
print ("~*~"*10)
print (Result_) # Print the Results which type is list
print ("~*~"*10)

Value = "1,2,6,45,6,4,abc,def" # Declare the Variable with Comma Seprated Values
print ("~*~"*5)
print ("Declare String Values :\t",Value)
print (type(Value)) # Checking the Type (which is String)
print ("~*~"*5)
Split =  Value.split(",") # Using Spit removing the "," Commas
print ("~*~"*5)
print (Split) # Printing the Results in list format
print (type(Split)) #  Checking the Type (which is List Now Automatically done by python)
print ("~*~"*5)