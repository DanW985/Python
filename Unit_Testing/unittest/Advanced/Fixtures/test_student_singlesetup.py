"""

Creating the student instances at the class level by usint the setUpClass
We have included the setUp and tearDown functions with just print statements and not declaring any operations in these functions.

Because the instances of the students are being created at the Class level we cannot alter them in test functions. So we cannot modify the email address or the full names

"""

import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nsetupClass\n')
        cls.stu_1 = Student('Robin', 'Wills', '25000')
        cls.stu_2 = Student('Mark', 'Smith', '28000')

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    def setUp(self):
        print('\nsetUp')

    def tearDown(self):
        print('tearDown')

    def test_mail(self):

        print('test_mail')

        self.assertEqual(self.stu_1.mail, 'Robin.Wills@xyz.com')
        self.assertEqual(self.stu_2.mail, 'Mark.Smith@xyz.com')
    
    def test_fullname(self):

        print('test_fullname')

        self.assertEqual(self.stu_1.fullname, 'Robin Wills')
        self.assertEqual(self.stu_2.fullname, 'Mark Smith')

    def test_stipend_hike(self):

        print('test_stipend_hike')
        self.stu_1.apply_hike()
        self.stu_2.apply_hike()

        self.assertEqual(self.stu_1.stipend, 26250)
        self.assertEqual(self.stu_2.stipend, 29400)

    if __name__ == '__main__':
        unittest.main()