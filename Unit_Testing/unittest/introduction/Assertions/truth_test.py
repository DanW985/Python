"""

assertTrue takes one arg and tests if its True. If it is test will pass.
If it is not then the test will fail

assertFalse takes one arg and tests if its False. If it is test will pass.
If it is not the test will fail

"""

import unittest

class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue((5-2) == 3)

    def test_assert_false(self):
        self.assertFalse((5-2) == 4)

if __name__ == '__main__':
    unittest.main()