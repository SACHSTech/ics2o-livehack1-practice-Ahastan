'''
-------------------------------------------------------------------------------
Name:		f_to_c.py

Purpose:	Telling the user to input a tempreture in Fahrenheit and outputting the result in Celcius

Author:	Surees.A

Created:	03/12/2020
------------------------------------------------------------------------------
'''

# input: Ask the user what the degree is in fahrenheit
fahrenheit_degree = float(input("What is the temperature in Fahrenheit? "))
# processing: Calculate the conversions between fahrenheit to celcius
celcius = ((fahrenheit_degree - 32)*(5/9))
# output: print the coversions and tell the user the conversion
print (str(celcius) + " degrees celcius is equivalent to " + str(fahrenheit_degree) , "degrees fahrenheit")