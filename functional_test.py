import unittest

from python_learn_pack.test1 import *

class FunctionTest(unittest.TestCase):
	"""docstring for FunctionTest"""

	def test_return_of_function(self):
		ret = returnfunc('hello')
		self.assertEqual('hello',ret)



if __name__ == '__main__':
	unittest.main()