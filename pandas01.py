# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:33:12 2024

@author: Student
"""
import pandas

file= pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())



#storing Data
B1=30
B2=40
B3=30
B4=49

print(B1)
print(B2)

file2= pandas.read_csv("iris.csv")
print(file2)
print(file2.info())
print(file2.describe())

file3= pandas.read_csv("diab_data.csv")
print(file3)
print(file3.info())
print(file3.describe())

file4= pandas.read_csv("housing_data.csv")
print(file4)
print(file4.info())
print(file4.describe())

file5= pandas.read_csv("insurance_data.csv",skiprows=5)
print(file5)
print(file5.info())
print(file5.describe())
