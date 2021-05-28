###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #7
# Program: test_leapyear.py
###############################

import unittest
#import leapyear


class testLeapYear(unittest.TestCase):

	def test_type(self):
		print("There SHOULD be an error if the type is correct")
		with self.assertRaises(ValueError): leapyear.main()


if __name__ == '__main__':
	unittest.main()
