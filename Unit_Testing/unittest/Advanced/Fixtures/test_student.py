"""

I have imported the Student class from the student.py file on line 8

Created 2 student instances stu1 and stu2 defining the first name, last name and the 
stipend

We then check that the actual emails of stu1 and stu2 match expected values based
on the property defined in student.py

We then alter the student instances by updating the first name, then check to ensure that 
the email addresses are updated as expected using the new values. With these tests we can prove that the mail function is performing as expected

We then create a new test function to test the full name property. In this test we again create two student instances and set the values for the expected fields

We then check that the fullname function correctly concats the first and last name of stu1 and stu2 and use the assertEquals to do this.

We then update the stu1 and stu2's first name and again use assertEquals to ensure that the actual full name matches the expected

The final test will be to check the stipend hike function. As with the tests above we have created to student instances and set the values to the expected fields

We then pass the stu1 and stu2 instances into the apply hike function and then perform an assert to check that the ouput(the actual) of that function matches the expected which we pass in

"""

import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_mail(self):

        stu_1 = Student('Robin', 'Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)

        self.assertEqual(stu_1.mail, 'Robin.Wills@xyz.com')
        self.assertEqual(stu_2.mail, 'Mark.Smith@xyz.com')

        stu_1.first = 'Jenifer'
        stu_2.first = 'Graham'

        self.assertEqual(stu_1.mail, 'Jenifer.Wills@xyz.com')
        self.assertEqual(stu_2.mail, 'Graham.Smith@xyz.com')
    
    def test_fullname(self):

        stu_1 = Student('Robin', 'Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)

        self.assertEqual(stu_1.fullname, 'Robin Wills')
        self.assertEqual(stu_2.fullname, 'Mark Smith')

        stu_1.first = 'Jenifer'
        stu_2.first = 'Graham'

        self.assertEqual(stu_1.fullname, 'Jenifer Wills')
        self.assertEqual(stu_2.fullname, 'Graham Smith')

    def test_stipend_hike(self):

        stu_1 = Student('Robin', 'Wills', 25000)
        stu_2 = Student('Mark', 'Smith', 28000)

        stu_1.apply_hike()
        stu_2.apply_hike()

        self.assertEqual(stu_1.stipend, 26250)
        self.assertEqual(stu_2.stipend, 29400)

    if __name__ == '__main__':
        unittest.main()


