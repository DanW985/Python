"""

To temporarily skip a test use the @unittest.skip decorator as shown with test
number 2. We can add a message as the argument to show why it is being skipped.

When you run the tests from the command line with -v you will see the message for
that is associated to the skipped test. It also shows the overall status plus a
skipped value

Conditionally skip tests - for example we can skip a test if the version of Python is
less than 3. To get the Python version we need to make use of the sys module

Added a new test test_skip_due_to_version and changed the length arg but kept the
bredth arg as 0

Added the skipIf decorator, we are checking that the first item in the list is the
version number is less than 3, the second arg is the message for skipping the test.
The test executes because I am using Python 3 so it does not meet the criteria for the 
test to be skipped.

To confirm that the test does get skipped due to the skipIf created a new test and 
changed the condition to if the version of Python is 3 or greater '>='. As expected
the test is skipped and the message is shown in the console.

Another decorator that can be used for skipping is skipUnless. To demo I have created
another test and attached this decorator to it. This test will be skipped unless the 
specific condition is met. To make this test fail I will say that the OS has to be 
darwin(MacOS).

Because I am running on a Windows machine this test has skipped as expected

"""

import unittest
import rectangle_perimeter
import sys

class TestArea(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(10, 5), 30)

    @unittest.skip('Temp skips error test')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 0)

    @unittest.skipIf(sys.version_info[0] <3,
                        'This test requires Python 3 or higher')
    def test_skip_due_to_version(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(15, 0)

    @unittest.skipIf(sys.version_info[0] >=3,
                        'This test requires Python 2 or lower')
    def test_skip_due_to_version1(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(9, 0)

    @unittest.skipUnless(sys.platform.startswith('darwin'),
                            'Requires MacOS')
    def test_skip_unless(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(8, 0)

if __name__ == '__main__':
    unittest.main()