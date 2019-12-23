#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        19th Problem : https://projecteuler.net/problem=19
#----------------------------------------------------------------

"""
	Function used to Increment days or monthes or years 
	####################################################################################
"""
def incrementYear():
	""" Increment the gobal "year" variable, Set LeapYear to 1 if the new year is a leap year. """
	global year
	year += 1
	if year%4 == 0 and (year%100 != 0 or year%400 == 0):
		LeapYear = True
	else:
		LeapYear = False

def incrementMonth():
	""" Increment the gobal "month" variable + reset the month counter. """
	global month
	month = month+1
	if month == 12:
		incrementYear()
		month = 0

def incrementDay():
	""" Increment the gobal "day" variable, and check if we change of month """
	global day, numberOfTheDay
	day = (day+1)%7
	numberOfTheDay +=1
	checkForVariationInMonth()

def checkForVariationInMonth():
	""" Used to check how many days do we have in a month and manage this month. """
	global month
	#Case of :30 days monthes
	if month == 3 or month ==5 or month == 8 or month == 10 :
		manageMonth(30)
	#Febuary Cases:
	elif month == 1 :
		manageFebuary()
	#Case of :31 days monthes
	else:
		manageMonth(31)


"""
	Manage monthes + the counter of sundays 
	####################################################################################
"""
def manageMonth(n) :
	""" Check if the actual number day "numberOfTheDay" is greater than the number of days that 
	there is in this month which is "n". """
	global numberOfTheDay
	if numberOfTheDay > n:
		incrementMonth()
		numberOfTheDay = 1

def manageFebuary():
	""" Special function for febuary as in leapyears it has 29 days. """
	global LeapYear
	nb_day_feb = 28
	if LeapYear == True :
		nb_day_feb += 1
	manageMonth(nb_day_feb)

def checkCounter():
	""" Check if we are the first of the month AND if we are a sunday. """
	global numberOfTheDay,day,counter
	if numberOfTheDay == 1 and day == 6:
		counter +=1

"""
	Print Stuff, AND test functions, not used in the main program, but
	can be usefull to debug if you try things.
	####################################################################################
"""
def printDate():
	global year,month, numberOfTheDay, day
	print ("day =",day,"//",numberOfTheDay,"th // mm=",month,"// y=",year)

def addXday(x):
	print ("Add ",x," day")
	for x in range(1,x+1):
		incrementDay()
	printDate()
	print("")


"""
	Main program:
	Initial state : Thursday 1 Januray 1901
	We begin the 2nd month --> friday 1 Febuary 1901
	cause : We need the loop condition to be : while month != 0:

	Days are not monday,tuesday etc... they are the index of the day beginning with 0:
	Monday = 0,  Tuesday=1 ..., Sunday = 6

	Same process is usde for monthes.
	January = 0, ..., December = 11
	####################################################################################
"""
year = 1901
LeapYear = False
month = 1
numberOfTheDay = 1
day = 4

# Number of Syndays that have been the 1st of the month
counter = 0

printDate()
while year < 2001:
	nextYear = year+1
	while month != 0 or year!=nextYear:
		incrementDay()
		checkCounter()

	print ("      **Year",year,"Done.")
	printDate()

print ("\nThe number of Sundays that fell the 1st of a month in the 20 century is :")
print ("    Number of Sundays = ",counter)
