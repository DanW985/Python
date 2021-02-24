"""

The init class is the constructor so when we create an instance of student
we will specify a first name, a last name and the initial stipend.
All these values will be stored in fields within this instance.

We have used the @property decorator to show where the properties have been 
created

We then use these values to create additional properties;
mail - a concatenation of the values stored in first and last appended with 
@xyz.com
fullname - a concatenation of the values stored in first '+space' last

We have defined an additional func. that applies the stipend hike of 5% by taking
the entered stipend value(int) and multiplying it by the fixed stipend_hike_rate

"""

class Student:

    stipend_hike_rate = 1.05

    def __init__(self, first, last, stipend):

        self.first = first
        self.last = last
        self.stipend = stipend
    
    @property
    def mail(self):
        return self.first + "." + self.last + "@xyz.com"

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_hike(self):
        self.stipend = int(self.stipend) * self.stipend_hike_rate