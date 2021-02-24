def get_perimeter(length, bredth):
    if length == 0 or bredth == 0:
        raise ValueError('Invalid Input!')
    return 2 * (length+bredth)