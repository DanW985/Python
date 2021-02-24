"""

In this demo we will intialize a test suite without any test cases and then adding them later.

Errors that occur in test suites will be output to the console.

If you want to add multiple tests to a test suite use the .addTests() method and add the test names you want to include in a list.

Using the makeSuite function. I have commented out lines 42 - 46 to use this new function.

The args to this function start with the class name where the tests are located, the second arg is the name of the suite which is set to 'test'.

When you run this suite the output will not contain the detail of the tests ran
used the suite.addTests function to add the remaining 4 tests

To see what the TextTestRunner returns we will create an object called result and use that to extract detailed test run information. The fields and their explanations are
result.errors - to capture any errors
result.failures - to capture and failures
result.skipped - to capture anu skipped tests
result.testsRun - to capture the number of tests run
result.wasSuccessful - boolean value - true if all tests pass, false if a single test fails

to enable verbose mode add verbosity=2 to the unittest.TextTestRunner

The output following this means the output now includes the name of the functions and their sequence 

creating a test to trigger a failure, however we are not expecting an error in this test so we will get a failure and an error entry from the result object we will also make one of the tests in this this suite skip.

The failure, the error and the skipped tests are now capture in the result object and output to the console

"""

import unittest

class TestMultiplication(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3 * 5), 12)

class TestAddition(unittest.TestCase):
    def runTest(self):
        self.assertEqual((1 + 5), 6)

class TestDivision(unittest.TestCase):
    def runTest(self):
        self.assertEqual((7 / 7), 1)

class TestDivisionToFail(unittest.TestCase):
    def runTest(self):
        self.assertEqual((7 / 0), 1)

class SimpleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    @unittest.skip('Temp skipping test')
    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)

    def test_4(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    """
    suite = unittest.TestSuite()

    suite.addTest(TestMultiplication())

    suite.addTests([TestAddition(), TestDivision()])
    """
    suite = unittest.makeSuite(SimpleTest, 'test')

    suite.addTests([TestMultiplication(), TestDivision(), TestDivisionToFail(), TestAddition()])

    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print('Errors: ', result.errors)
    print('\nFailures: ', result.failures)
    print('\nSkipped Tests: ', result.skipped)
    print('\nNo. of Tests: ', result.testsRun)
    print('\nWas it a successful test? ', result.wasSuccessful())