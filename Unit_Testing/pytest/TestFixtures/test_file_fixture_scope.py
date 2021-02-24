"""

This scope ensures that the fixture is only executed once and not each time
a test runs
Yield in a fixture means the lines preceeding the keyword will be executed at the 
start of the scope and the lines after the keyword will be run at the end of the 
scope

When you run this file through the command line with -s command you can see that the 
opening and closing prints only occur at the start and the end of the tests

If you remove the scope the results in the command line will still pass however
the commentary (running order is different)
first test called
Creating File prints
It writes 10 lines 
Test Passed
It closes the file

second test called
Creating File prints
It writes 10 lines 
Test Passed
It closes the file

"""

import pytest
import os

@pytest.fixture(scope = 'module')
def test_file():
    print('\nCreating file')
    f = open('test_file.txt', 'a+')
    yield f

    print('\nClosing file')
    f.close()

def test_write_ten_lines(test_file):
    print('\nWriting 10 lines')
    num_lines_before = sum(1 for line in open(test_file.name))

    for i in range(10):
        test_file.write('X Y Z %d\n' % (i+1))

    test_file.flush()
    num_lines_after = sum(1 for line in open(test_file.name))

    assert (num_lines_after - num_lines_before) ==10

def test_file_size_on_write(test_file):
    print('\nWriting one line')
    size_before = os.stat(test_file.name).st_size

    test_file.write('A B C 1\n')
    test_file.flush()

    size_after = os.stat(test_file.name).st_size

    assert (size_after - size_before) > 0