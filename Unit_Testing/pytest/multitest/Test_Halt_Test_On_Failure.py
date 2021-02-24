"""
we are going to make a test fail
to stop execution add the '-x' to the command... this will now run the first test
but stop at the second
pytest -v -x Test_Halt_Test_On_Failure.py
An iterative approach could be taken here to fix the bugs as they arrise OR see all
failed tests at once

You can add a tolerance of failures to the execution by adding the following flag
--maxfail=<numberoffailures>
IE the following command would allow two tests to fail before execution is stopped
pytest -v -x --maxfail=2 Test_Halt_Test_On_Failure.py
This means that all four tests will run as the tolerance has not been exceeded

To supress the failure information add this command --tb=no
'tb' = traceback 
other accepted tb commands;
--long, --short(default)
pytest -v -x --maxfail=2 --tb=no Test_Halt_Test_On_Failure.py

"""

def test_type():
    assert type(1 + 2) is int

def test_add_int():
    assert 5 + 2 == 9

def test_another_sum():
    assert 1 + 3 == 5 

def test_string():
    assert 'u'  in 'sun'

def test_another_string():
    assert 'i' in 'sun'

def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'

