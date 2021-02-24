"""

We are only going to be looking at the add function within the cal1 module

In Python we can pass different data types to the add function as shown below
Testing the add function with the following Data Types;
Integer
Floats
Strings

In Pytest we can parameterize a call to a function

"""
import cal2 

def test_add_int():
    result = cal2.add(5, 2)
    assert result == 7

def test_add_float():
    result = cal2.add(3.2, 2.4)
    assert result == 5.6

def test_add_string():
    result = cal2.add('winter', ' '+ 'season' )
    assert result == 'winter season'