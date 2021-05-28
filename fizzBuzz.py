###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #7
# Program: fizzBuzz.py
###############################



def main():
	x = 1
	thirty = ""
	while x <= 100:
		fifteen = x % 15
		three = x % 3
		five = x % 5
		if fifteen == 0:
			print("FizzBuzz")
		elif three == 0:
			print("Fizz")
		elif five == 0:
			print("Buzz")
		else:
			print(x)
		x = x + 1
	return x


if __name__ == '__main__':
	main()
