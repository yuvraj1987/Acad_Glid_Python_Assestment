# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:05:12 2018

@author: jkdadhich
"""

Max_Range = 5       # Define how many item Value to print '*' in both direction
Value = "*"         # Define what needs to be printed over screen
Start_Range = 0     # Starting Point

# Below method is little bit tricky one Using While loop
while Start_Range <= Max_Range:  # Checking Condtion when while loop stop iteration

    Start_Range = Start_Range+1 # increment the Count by One

    print (Value*Start_Range)   # Print value '*' and multiply by count of iteration update

    if Start_Range == 5:      # if will check with highest number which will declare above

        while Max_Range >0: # Making while as reveresd the count

            Max_Range = Max_Range -1 # Setting value in decreasing order

            print (Value*Max_Range)  # Print value '*' and multiply by count of iteration update


"""NOTE : Below two method as easy seem but tricky as well """
Max_Range = 5 # Define how many item Value to print '*' in both direction

# Using For loop once upward and downward at same time
# list will be created this ways[ 0,1,2,3,4,5,4,3,2,1,0]
# print the value which you want over screen multipy number of iteration
for i in list(range(Max_Range+1)) + list(reversed(range(Max_Range))):
    print (Value*i)


# Same down above instead of list used tuple (operation will remain same)
for i in tuple(range(Max_Range+1)) + tuple(reversed(range(Max_Range))):
    print (Value*i)