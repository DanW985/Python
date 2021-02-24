"""

when running multiple unit tests from the command line just enter the name of the .py file
you want to execute. Add -v to make the output more verbose

"""

import unittest

class Testing(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('beta'.upper(), 'BETA')

    def test_boolean(self):
        x = True
        y = True
        self.assertEqual(x, y)

    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('Beta'.isupper())
    
if __name__ == '__main__':
    unittest.main()


