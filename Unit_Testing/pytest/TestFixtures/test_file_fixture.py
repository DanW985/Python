"""

We can create files using the OS module

The fixture decorator indicates that the function that is defined, the func. will
execute before each test is ran and the value returned can be accessed by the
individual test funcs. In this case f

'a+' = append mode

Steps for test_write_ten_lines;
The fixture opens the file in append mode
When the test starts it prints a line
Then counts the number of lines in the file and assigns that figure to
num_lines_before
Then in the for loop which has a range of ten it will write XYZ followed by a line No
into the test_file
test_file.flush ensures all changes are written and saved
Then counts the number of lines in the file and assigns it to the variable
num_lines_after
Then asserts the difference between after and before equals to 10
Then closes the file

Steps for test_file_size_on_write
The fixture opens the file in append mode
Prints 'writing one line'
Makes use of stat(st.size) to count the file size and stores it the variable 
size_before
Writes another line containing 'A B C 1' 
Writes the changes and saves them in test_file.flush()
Makes use of stat(st.size) to count the file size and stores it the variable
size_after
Then checks that after - before is greater than (>) 0
Then closes the file

Use the -s flag to show print statements and running order

The default scope of the fixture is at the function level, we can however set the
scope of the fixture

"""

import pytest
import os

@pytest.fixture
def test_file():
    print('\nCreating file')
    f = open('test_file.txt', 'a+')
    return f

def test_write_ten_lines(test_file):
    print('\nWriting ten lines')
    num_lines_before = sum(1 for line in open(test_file.name))

    for i in range(10):
        test_file.write('X Y Z %d\n' % (i+1))

    test_file.flush()
    num_lines_after = sum(1 for line in open(test_file.name))

    assert (num_lines_after - num_lines_before) == 10
    test_file.close()

def test_file_size_on_write(test_file):
    print('\nWriting one line')
    size_before = os.stat(test_file.name).st_size

    test_file.write('A B C 1\n')
    test_file.flush()

    size_after = os.stat(test_file.name).st_size
    assert (size_after - size_before) > 0
    test_file.close