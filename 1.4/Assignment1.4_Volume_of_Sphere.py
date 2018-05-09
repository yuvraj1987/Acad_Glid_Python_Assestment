# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:18:35 2018

@author: jkdadhich
"""

import math  # Import math library for Using mathematical caluation (Standard Value)

Diameter_of_Sphere  = 12 # Provide by Question Change as per requirement or test

# Diameter = twice of Radius
Radius_of_Sphere    =  Diameter_of_Sphere/2 # Extracting Radius from Diameter

# From Math Library import Pie Value (22/7) = 3.14 approx.
pie_Value           =  math.pi # 22/7

# From Math Library Use Power Method to get Cube of Any Value
# In this Case We are caluating the Cube of Radius
Cube_of_Radius      =  math.pow(Radius_of_Sphere,3)

# Formula for Volume of Sphere = (4/3)*(22/7) *cube of Radius

Volume_of_Sphere = (4/3)*(pie_Value)*(Cube_of_Radius) # Passing the Value in Formula

# Printing the Result with Volume of Sphere , Radius and Diameter
# Round of Value print over Screen
print ("\n Here is Volume_of_Sphere : '{}' whose Radius is : '{}' and Diameter is : '{}'".format(round(Volume_of_Sphere,4),round(Radius_of_Sphere,2),round(Diameter_of_Sphere,2)))




