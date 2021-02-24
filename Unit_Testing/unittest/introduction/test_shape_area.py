"""

Creating a test case to test multiple functions within a source

To run only one test, enter the following command

python -m unittest -q <module_name>.py.<class_name>.<function_name> -v

in this case to run the test_square only enter the command;
python -m unittest -q test_shape_area.TestArea.test_square -v

To run two of the three tests for example test_rectangle and test_square enter this 
command

-m unittest -q test_shape_area.TestArea.test_square test_shape_area.TestArea.test_rectangle -v

"""
import unittest
import shape_area

class TestArea(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(shape_area.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(shape_area.rectangle(6, 7), 42)
    
    def test_square(self):
        self.assertEqual(shape_area.square(7), 49)

if __name__ == '__main__':
    unittest.main()