#!usr/bin/env python
import os
import numpy

myFileName = "housing.data.txt"

data = [];
CRIM = [];
ZN = [];
INDUS = [];
CHAS = [];
NOX = [];
RM = [];
AGE = [];
DIS = [];
RAD = [];
TAX = [];
PTRATIO = [];
BRATIO = [];
LSTAT = [];
MEDV = [];

if os.path.isfile(myFileName):
	print(myFileName + " exists")
else:
	print(myFileName + " does not exist")
with open(myFileName, 'r') as file_handle:
	for  line in file_handle.readlines():
		line_clean = line.replace ('   ',' ').replace('  ', ' ')
		line_clean = line_clean.strip()
		values = line_clean.split(' ')
		for value in values:
			data.append((float(value)))

print ("Printing CRIM values")
for i in range(0, len(data), 14):
	CRIM.append(data[i])
print (CRIM)
	
print ("Printing ZN values")
for i in range(1, len(data), 14):
	ZN.append(data[i])
print(ZN)

print ("Printing INDUS values")	
for i in range(2, len(data), 14):
	INDUS.append(data[i])
print(INDUS)

print ("printing CHAS values")
for i in range(3, len(data), 14):
	CHAS.append(data[i])
print(CHAS)

print ("Printing NOX values")
for i in range(4, len(data), 14):
	NOX.append(data[i])
print(NOX)

print ("Printing RM values")
for i in range(5, len(data), 14):
	RM.append(data[i])
print(RM)

print ("Printing AGE values")
for i in range(6, len(data), 14):
	AGE.append(data[i])
print(AGE)

print ("Printing DIS values")	
for i in range(7, len(data), 14):
	DIS.append(data[i])
print(DIS)

print ("Printing RAD values")
for i in range(8, len(data), 14):
	RAD.append(data[i])
print(RAD)

print("Printing Tax values")
for i in range(9, len(data), 14):
	TAX.append(data[i])
print(TAX)

print ("Printing PTRATIO values")
for i in range(10, len(data), 14):
	PTRATIO.append(data[i])
print(PTRATIO)

print ("Printing BRATIO values")	
for i in range(11, len(data), 14):
	BRATIO.append(data[i])
print(BRATIO)

print("Printing LSTAT values")	
for i in range(12, len(data), 14):
	LSTAT.append(data[i])
print(LSTAT)

print("Printing MEDV values")
for i in range(13, len(data), 14):
	MEDV.append(data[i])
print(MEDV)

print("finished!")	

# for homework: 
#identify what type of data each value is, and cast it
#to the appropriate type, then print the new, properly-typed 
#list to the screen
