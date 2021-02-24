"""

we have imported the triangle_area source
changed the name of test_triangle to runTest

"""

import unittest
import triangle_area

class TestArea(unittest.TestCase):

    def runTest(self):
        result = triangle_area.triangle(10, 5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()