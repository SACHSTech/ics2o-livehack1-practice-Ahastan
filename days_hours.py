'''
-------------------------------------------------------------------------------
Name:		days_hours.py
Purpose:	Telling the user to enter an amount of hours and convert it into days

Author:	Surees.A
f
Created:	03/12/2020
------------------------------------------------------------------------------
'''

# Ask the user how many hours to input
hours = int(input("How many hours do you want to input? "))
# Calculate the number of hours into days
days = (hours/24)
remainder = (hours%24)
# Display the days for the user
days_rounded = (days//1)
print (str(hours) , "hours is equivalent to" , str(days_rounded) , ("days and") , str(remainder) , "hours")