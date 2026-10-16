
import math
from triangle import is_valid_triangle, classify_triangle


def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5)
    assert not is_valid_triangle(1, 1, 2)
    assert not is_valid_triangle(-1, 2, 3)
    assert not is_valid_triangle(0, 2, 3)


def test_classify_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_classify_isosceles():
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(4, 3, 3) == "Isosceles"
    assert classify_triangle(3, 4, 3) == "Isosceles"


def test_classify_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 4, 3) == "Right Scalene"
    assert classify_triangle(4, 5, 3) == "Right Scalene"
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_classify_invalid():
    assert classify_triangle(1, 1, 2) == "Invalid"
    assert classify_triangle(-1, 2, 3) == "Invalid"
    assert classify_triangle(0, 2, 3) == "Invalid"


def test_right_triangle_non_integer():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
