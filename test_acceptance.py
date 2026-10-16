from triangle import classify_triangle

def test_customer_requirements():
    # Check if the measurements make an invalid triangle
    assert classify_triangle(2, 3, 6) == "Invalid"

    # Check if two equal sides are classified correctly
    assert classify_triangle(6, 6, 8) == "Isosceles"

    # Check if a right triangle is identified
    assert classify_triangle(5, 12, 13) == "Right Scalene"
