"""

To use a test suite please see line 19. We use the unittest.TestSuite base class, enter the names of the functions we want to call and store them into a variable named suite.
We then pass that variable into the unittest.TextTestRunner().run(suite) command

The test cases are contained in a list []

TextTestRunner = simple implementaion of a test runner, which like a test runner orchestrates the tests to be ran in the suite.

The results of the tests that are ran in the .run() method will be printed to standard out

When you use a test runner an effect of that is even if you have the verbose flag enabled the information in the console does not contain test execution information

"""
import unittest

class TestString(unittest.TestCase):

    def runTest(self):
        self.assertEqual( 'a'*4, 'aaaa')

class TestUCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual('gama'.upper(), 'GAMA')

if __name__ == '__main__':

    suite = unittest.TestSuite([TestString(), TestUCase()])
    unittest.TextTestRunner().run(suite)
    