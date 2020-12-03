'''
-------------------------------------------------------------------------------
Name:		windcill.py
Purpose:  Finding the tempreture and wind speed, and converting it into the windchill factor

Author:	Surees.A

Created:	03/12/2020
------------------------------------------------------------------------------
'''

# Find the tempreture and wind speed
temprature = int(input("Enter the temprature in Celcius: "))
wind_speed = int(input("Enter the wind speed: "))
# Process numbers in the formula
wind_chill_factor = 13.12 + (.6215*temprature) - (11.37*wind_speed**0.16) + (.3965*temprature*wind_speed**0.16)
# Output the numbers 
wind_chill_factor_rounded = (wind_chill_factor//1)
print (wind_chill_factor_rounded)