"""

This class derives the base class unittest.TestCase
There can be multiple defined test functions in one class

"""

import unittest

class Testing(unittest.TestCase):

    def test_string(self):
        x = 'alpha'
        y = 'alpha'
        self.assertEqual(x, y)

if __name__ == '__main__':

    unittest.main()