###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #7
# Program: leapyear.py
###############################


def main():
	year = input("Please enter a year: ")
	year = int(year)
	fourYears = year % 4
	hunYears = year % 100
	fohunYears = year % 400

if __name__ == '__main__':
	main()
