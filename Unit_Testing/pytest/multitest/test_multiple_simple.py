"""
use pytest -v to show the running order of the tests in the console

to only execute the 'test_type' test run the following in command line
pytest -v  <module_name>.py::<function_name>

to run tests that contain the word 'add' run the following in command line
pytest -v -k _<function_name_argument> this could be 'string', 'add'
'add' would run test_add_int and test_add_string
'string' would run test_string and test_add_string

to use multiple substring arguments run the following
pytest <module_name>.py -v -k "<substring1> or <substring2>" ie "add or string" 
will run three tests out of the four as these three contain the specific substrings

if you passed the substrings "add and string" this would only run the 'test_add_string'
function as the fuction name meets BOTH substring args
"""


#using assert to check that the result of the sum is of Integer type
def test_type():
    assert type(1 + 2) is int

#checks the result of an addition
def test_add_int():
    assert 5 + 2 == 7

#asserts that a specific letter appears in a supplied string
def test_string():
    assert 'u'  in 'sun'

#asserts that two strings concatenated equal a new string
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'