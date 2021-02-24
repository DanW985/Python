"""

The setUp function is within the unittest framework which is invoked for every single test defined within a test case.

This setUp function will be called first, then the following defined operations will be run. We use this function to hold all the code that does some kind of initialization for the tests.

We then add a tearDown function which is executed at the end of every test within the test case. Typically you would use the tearDown function to hold common clean up operations after each test. In this example we are just storing the pass keyword

We then go on to add the same test cases that exist in test student however we do not need to create the instance of student as this has been handled in the setUp function

To verify the order of execution for each of the functions within the test script, I've added a series of print statements

"""

import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):

        print('\nsetUp')
        self.stu_1 = Student('Robin', 'Wills', '25000')
        self.stu_2 = Student('Mark', 'Smith', '28000')

    def tearDown(self):
        print('tearDown')
        

    def test_mail(self):

        print('test_mail')
        self.assertEqual(self.stu_1.mail, 'Robin.Wills@xyz.com')
        self.assertEqual(self.stu_2.mail, 'Mark.Smith@xyz.com')

        self.stu_1.first = 'Jenifer'
        self.stu_2.first = 'Graham'

        self.assertEqual(self.stu_1.mail, 'Jenifer.Wills@xyz.com')
        self.assertEqual(self.stu_2.mail, 'Graham.Smith@xyz.com')

    def test_fullname(self):

        print('test_fullname')
        self.assertEqual(self.stu_1.fullname, 'Robin Wills')
        self.assertEqual(self.stu_2.fullname, 'Mark Smith')

        self.stu_1.first = 'Jenifer'
        self.stu_2.first = 'Graham'

        self.assertEqual(self.stu_1.fullname, 'Jenifer Wills')
        self.assertEqual(self.stu_2.fullname, 'Graham Smith')

    def test_stipend_hike(self):

        print('test_stipend_hike')
        self.stu_1.apply_hike()
        self.stu_2.apply_hike()

        self.assertEqual(self.stu_1.stipend, 26250)
        self.assertEqual(self.stu_2.stipend, 29400)

    if __name__ == '__main__':
        unittest.main()
    

    

