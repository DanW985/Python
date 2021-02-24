"""

@pytest.mark decorator allows you to 'tag' a script or scripts
To run tests that are associated with a specific marker 'tag'

To gain access to pytest.mark you need to import pytest into the src file

To run the tests that have the marker 'number' run the following command
pytest -v -m number Test_test_markers_and_skipping_tests.py

This will result in two tests being selected and ran whilst 2 are not run

To run the tests with the marker 'string' run the following command
pytest -v -m string Test_test_markers_and_skipping_tests.py

This will result in two tests being selected and ran whilst 2 are run

.number and .string are custom markers which will throw warnings in the command line.

To skip a test you can use the skip marker @pytest.mark.skip
pytest -v Test_test_markers_and_skipping_tests.py
You can add a reason to the skip mark to show why it is not being run
To capture the skipped reason in the output add the -rs flag to the command
pytest -v -rs Test_test_markers_and_skipping_tests.py
This will show the name of the function(test) that was skipped and the reason why

Running all the tests without specifying any markers will output that 4 have passed
and 1 is skipped

You can add details of the test failure to the output, changing test_add_int to make it fail for this
example.
To do this add 'f' to the 'r' command
The command for this is
pytest -v -rf Test_test_markers_and_skipping_tests.py - this will only include failed test details
To include both 's'kipped and 'f'ailed tests the full command is
pytest -v -rsf Test_test_markers_and_skipping_tests.py

Changing the test_add_int to remove the failure and removed the 'number' and 'string' custom markers
from the other tests

Further arguments to pass
-q = quiet mode - this outputs '..s.'  and the results of the tests
pytest -q Test_test_markers_and_skipping_tests.py

When you run the above command with the -v (verbose) flag you will see details of 
platform being used, version of Python, version of Pytest being used and the location of the module
quiet mode strips out the details of the tests that were run
pytest -v -q Test_test_markers_and_skipping_tests.py
 

"""
import pytest

def test_type():
    assert type(1 + 2) is int

def test_add_int():
    assert 5 + 2 == 7

@pytest.mark.skip(reason='Temporarily Disabled')
def test_string():
    assert 'u'  in 'sun'

def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'