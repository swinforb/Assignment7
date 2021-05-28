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
		size = fizzBuzz.main()
		self.assertEqual(size, 101)


if __name__ == '__main__':
	unittest.main()


