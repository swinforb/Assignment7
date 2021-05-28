###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #7
# Program: test_fizzbuzz.py
###############################

import unittest
import fizzBuzz


class testFizzBuzz(unittest.TestCase):


	def test_size(self):
		ans = fizzBuzz.main()
		size = ans[0]
		self.assertEqual(size, 101)

	def test_value_30(self):
		ans = fizzBuzz.main()
		thirty = ans[1]
		self.assertEqual(thirty, "Fizz")



if __name__ == '__main__':
	unittest.main()


