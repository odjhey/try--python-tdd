

import unittest


def add(x, y):
	return x+y

class TestSome (unittest.TestCase):
	def test_t1(self):
		expect = 10
		result = add(2,8)
		self.assertEqual(expect, result, "Should be 10")


if __name__ == '__main__':
	unittest.main()
