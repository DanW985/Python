"""

assertEqual - takes in two args for anything that could be evaluated
objects/litterals

assertnotEqual - takes in two args for anything that could be evaluated
objects/litterals

In this example it is using both litteralls and objects which have ensured they will
pass

"""

import unittest

class EqualityTest(unittest.TestCase):

    def test_not_equal(self):
        self.assertEqual(6, 8-2)

    def test_equal(self):
        self.assertNotEqual(7, 4*2)


if __name__ == '__main__':
    unittest.main()