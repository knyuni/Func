""" calculate number"""

import unittest

from calc import add_numbers  

class TestAddNumbers(unittest.TestCase):
	@unittest.skip("WIP")

	def test_input_is_number(self):
		self.assertRaises(TypeError, str)
			

	def test_works_correctly(self):
		self.assertEquals(add_numbers(3),6)

if __name__ == '__main__':
    unittest.main()