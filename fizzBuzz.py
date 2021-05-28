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
			if x == 30:
				thirty = "FizzBuzz"
		elif three == 0:
			print("Fizz")
			if x == 30:
				thirty = "Fizz"
		elif five == 0:
			print("Buzz")
			if x == 30:
				thirty = "Buzz"
		else:
			print(x)
			if x == 30:
				thirty = str(x)
		x = x + 1
	ans = (x, thirty)
	return ans


if __name__ == '__main__':
	main()
