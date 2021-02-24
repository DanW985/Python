def rectangle_perimeter(length, bredth):
    return 2 * (length + bredth)

def test_perimeter():
    assert rectangle_perimeter(5,7) == 24