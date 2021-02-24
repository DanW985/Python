"""

changed test_add_int to make it fail
to trigger the debugger when a failure is encountered and the following flag
--pdb
The PDB is now displayed showing details of the failed test.
At this moment the skip test and the following test is not run
To continue with execution type cont
the full command is
pytest --pdb Test_Pytest_Debugger.py
To enable the debugger for all tests user the flag --trace
The full command is
pytest --trace Test_Pytest_Debugger.py
use 'cont'inue to proceed with execution in pdb 


"""
import pytest

def test_type():
    assert type(1 + 2) is int

def test_add_int():
    assert 5 + 2 == 9

@pytest.mark.skip(reason='Temporarily Disabled')
def test_string():
    assert 'u'  in 'sun'

def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'