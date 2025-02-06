"""
Week 2 (Grader - polysum)
"""

# A regular polygon has `n` number of sides. Each side has length `s`.
#
#   The area of a regular polygon is: (0.25 * n * (s * s)) / (tan(π/n))
#   The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called `polysum` that takes 2 arguments, `n` and `s`. This
# function should sum the area and square of the perimeter of the regular
# polygon. The function returns the sum, rounded to 4 decimal places.

import math

def polysum(n, s):
  """Calculates the sum of the area and the square of the perimeter of a regular
  polygon.

  A regular polygon has all sides of equal length and all angles between sides
  equal.

  Parameters:

    n (int): The number of sides of the polygon. Must be a positive integer.
    s (float): The length of each side of the polygon. Must be a positive
    number.

  Returns:

    float: The sum of the area and the square of the perimeter of the polygon,
    rounded to 4 decimal places.

  Formula:

    1. Area of a regular polygon:
        area = (0.25 * n * s^2) / tan(π / n)
    2. Perimeter of a regular polygon:
        perimeter = n * s
    3. polysum = area + (perimeter)^2

  Examples:

    >>> polysum(4, 5)  # Square with 4 sides of length 5
    162.5
    >>> polysum(6, 2)  # Hexagon with 6 sides of length 2
    90.6913
  """
  area = (0.25 * n * s) / math.tan(math.pi / n)
  perimeter = n * s
  polysum = area + (perimeter ** 2)
  return round(polysum, 4)

print(polysum(4, 5))  # Square with 4 sides of length
print(polysum(6, 2))  # Hexagon with 6 sides of length
