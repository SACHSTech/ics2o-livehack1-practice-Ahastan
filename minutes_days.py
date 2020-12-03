'''
-------------------------------------------------------------------------------
Name:		minutes_days.py
Purpose:	Converting the minutes into days and hours

Author:	Surees.A

Created:	03/12/2020
------------------------------------------------------------------------------
'''

# ask the user how many minutes they want to input
minutes = int(input("How many minutes do you want to input? "))
# process the minutes into days and hours
# hours
hours = (minutes/60)
hours_remainder = (minutes%60)
hours_rounded = (hours//1)
# days
days = (minutes/1440)
days_remainder = (minutes%1440)
days_rounded = (days//1)
#minutes
minutes = (minutes)
# output the data using print
print (str(hours_rounded) , "hour and" , str(hours_remainder) , "minutes")
print (str(days_rounded) , "days and" , str(days_remainder) , "minutes")
print (str(minutes) , "minutes")