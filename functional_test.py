import unittest

from python_learn_pack.test1 import *

class FunctionTest(unittest.TestCase):
	"""docstring for FunctionTest"""

	def test_return_of_function(self):
		ret = returnfunc('hello')
		self.assertEqual('hello',ret)

	def test_floor_div(self):
		ret = floordiv(6,4)
		self.assertEqual(1,ret)

	def test_func_ret_multi_value(self):
		y,x = testfuncreturnmultivalue(100,12)
		self.assertEqual(y,12)
		self.assertEqual(x,100)

if __name__ == '__main__':
	unittest.main()