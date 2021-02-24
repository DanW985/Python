"""
by placing these fixtures in this file we are making them accessible
to any test scripts in the same directory as this conftest file

write file prints creating file
opens a file in write mode
writes X Y Z 10 times on a new line each time
flushes the file
yiels the filepointer
prints closing file on a new line
closes the file
fixutre is using default scope of function

readonly_file prints creating file
opens a file in write mode
writes X Y Z 10 times on a new line each time
closes the file
opens the file again in read mode
yields the file pointer
prints a line
closes the file

"""

import pytest
import os

@pytest.fixture
def write_file():
    print('\nCreating file')
    f = open('append_file.txt', 'w+')

    for i in range(10):
        f.write('\nX Y Z %d' % (i+1))

    f.flush()

    yield f

    print('\nClosing file')
    f.close()

@pytest.fixture
def readonly_file():
    print('\nCreating file')
    f = open('readonly_file.txt', 'w+')

    for i in range(10):
        f.write('\n X Y Z %d' % (i+1))

    f.close()

    f=open('readonly_file.txt', 'r')

    yield f

    print('\nClosing file')
    f.close()
