###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #7
# Program: leapyear.py
###############################


def main():
	result = 2
	year = input("Please enter a year: ")
	year = int(year)
	fourYears = year % 4
	hunYears = year % 100
	fohunYears = year % 400
	if fourYears == 0 and hunYears != 0 or fohunYears == 0:
		result = 1
	else:
		result = 0
	return result

if __name__ == '__main__':
	main()
