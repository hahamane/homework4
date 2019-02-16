#usr/bin/env python
import os
import numpy
import math
## Asking the file location which stores the data to analyze
fileLocation = input("What is your file location?")

## Creating array to store data
data = [];
final_data =[];
mean = [];
std = [];


## try/except is used to open the file and store the data
## in the array. However, if the file does not exist, instead
## of throwing an error, it will print that the location does
## not exist

try:
	with open (fileLocation, 'r') as file_handle:
		splitter = input("How are the data splitted?")
		for line in file_handle.readlines():
			line_clean = line.strip()
## As the data is separated by 'splitter', it is required to
## clean the data before storing them in their respective
## arrays.
			values = line_clean.split(splitter)
			for value in values:
				data.append(value)

## It is essential to ask how many columns are there to split
## data by its columns		

	column = int(input("how many different data are there? "))
## If there is a title row, we need to not include it in 
## the list.
	answer = input("Is there a title row? Y/N ")
	if(answer == 'y' or answer =='Y'):
		addition = int(column)
	else:
		addition = int(0)
	
	for i in range (0, column):
		scrap = [];

## total will be the total of a column
		total = 0
		
		for k in range (i+addition, len(data), column):
			scrap.append(float(data[k]))
			total += float(data[k])
			
		final_data.append(scrap)

## Calculating mean.

		mean.append(total/len(scrap))

## To calculate the standard deviation, it is needed to 
## re-run the loops due to the formula. It is needed to
##1. Work out the Mean (the simple average of the numbers)
##2. Then for each number: subtract the Mean and square 
## the result
##3. Then work out the mean of those squared differences.
##4. Take the square root of that and we are done!
	
	for i in range (0, column):
		averageSquare = 0
		for k in range (i, len(final_data[i])):
			
			averageSquare += (final_data[i][k]-mean[i])**2
			stdevation = math.sqrt(averageSquare/len(final_data[i]))
			
		std.append(stdevation)
	print("Printing average of columns")
	
	for i in range(0, len(mean)):
		print(mean[i])
	print("Printing standard deviations of columns")
	
	for i in range(0, len(std)):
		print(std[i])
except FileNotFoundError:
	print (fileLocation + " does not exist")


