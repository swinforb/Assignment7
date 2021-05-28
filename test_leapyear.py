###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: #7
# Program: test_leapyear.py
###############################

import unittest
import leapyear


class testLeapYear(unittest.TestCase):

	def test_type(self):
		print("There SHOULD be an failure if the type is correct, not an error")
		with self.assertRaises(ValueError): leapyear.main()

	def test_correctness(self):
		ans = leapyear.main()
		expect = input("Is the year you entered a leap year? (y/n): ")
		if expect == "y":
			exAns = 1
		elif expect == "n":
			exAns = 0
		self.assertEqual(exAns, ans)

if __name__ == '__main__':
	unittest.main()
