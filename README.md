# Triangle Classifier

## Overview
This project uses Python to classify triangles based on three side lengths. It checks whether a triangle is valid, identifies its type, and determines if it is a right triangle.

## Running the Tests
Install pytest and run the tests using:

`python3 -m pip install -r requirements.txt`

`python3 -m pytest -v`

All 7 tests passed.

## Test Cases and Boundaries
The tests cover the main triangle types: equilateral, isosceles, scalene, and right triangles. I also tested invalid inputs, including negative sides, zero-length sides, and the degenerate case (1, 1, 2), where two sides add up to the third. The non-integer case (5, 5, 5 × √2) checks floating-point tolerance.

An equilateral triangle cannot be a right triangle because all three angles are 60°, while a right triangle must have a 90° angle.

## Copilot Review Log

| Test | Copilot? | Decision | Reason |
|---|---|---|---|
| Valid triangle | Yes | Edited | Simplified the Boolean assertions. |
| Equilateral | Yes | Kept | Correctly checked equal sides. |
| Isosceles | Yes | Kept | Covered all positions of the equal sides. |
| Scalene | Yes | Edited | Copilot missed the non-right scalene case, so I added (4, 5, 6). |
| Invalid | Yes | Kept | Correctly checked invalid measurements. |
| Non-integer right | Yes | Edited | Changed the example to (5, 5, 5 × √2) to test floating-point tolerance. |

## Acceptance Criteria
1. For sides (2, 3, 6), the program must return "Invalid" because the measurements cannot form a triangle.
2. For sides (6, 6, 8), the program must return "Isosceles" because two sides are equal.
3. For sides (5, 12, 13), the program must return "Right Scalene" to identify a piece requiring reinforced corners.

## AI Use Disclosure

I used GitHub Copilot to generate suggestions for the unit tests, which I reviewed and modified where needed. I also used ChatGPT for coding guidance and troubleshooting. I checked the results using pytest. GitHub Copilot was not used for the acceptance test.