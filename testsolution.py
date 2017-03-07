import unittest
from tdd import *
class Prime_Testcase(unittest.Test_Solution):
	def print_primenumbers_below_10(self):
		self.assertTrue(Solution(10), 2,3,5,7)

	def print_primenumbers_below_10(self):
		self.assertTrue(Solution(7), 2,3,5,7)

	def testif_integer(self):
		self.assertTrue(Solution('prime')," error is returned")

	def print_primenumber_below_1(self):
		self.assertTrue(Solution(1),"none")

	def test_for_negative_integer(self):
		self.assertTrue(Solution(-9),"none")

	def test_if_list(self):
		self.assertTrue(Solution([1,6,7]),"error is returned")
	



