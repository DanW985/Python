"""

test_perimeter is to ensure that the correct value of the perimeter is returned
when the 'l'ength and 'b'readth (params) are passed in. As we have l = 10 and b = 5
we are expecting a value of 30 which is l + b * 2

test_error is to check the error handling in the get_perimeter funcion.
we are passing in 0 for bredth and this should throw a Value Error with the message
"Invalid Input!"

Because we are expecting an error the second test passes as we have handled the 
error

The arguments in the second test are not being passed to the get_perimeter function
but are being passed directly to the assertRaises function

To make the second test fail, change the 0 argument to 5. Because no valueError
exception is created(which is the expected behaviour) the test will fail. It
produces a message in the console "AssertionError: ValueError not raised by 
get_perimeter"

A new test has been created to use the 'with' block. Following the with block
a call is made to self.assertRaises(<expectedExceptionName>). It then calls the
function rectangle_perimeter.get_perimeter and passes a 0 arg for bredth.

The test will pass as the second test has raised the error as expected. This is a 
more intuitive way of writing the test

Created a 4th test to check that an error can be caught, it is the same as test 3 
except we are not passing in a 0 value. As expected because the fourth test does
not throw the expected error the test fails


"""

import unittest
import rectangle_perimeter

class TestArea(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(10, 5), 30)

    def test_error(self):
        self.assertRaises(ValueError,
                            rectangle_perimeter.get_perimeter,
                            10, 5)

    def test_error1(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 0)

    def test_error2(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 5)

if __name__ == '__main__':
    unittest.main()