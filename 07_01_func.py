def ping():
    return "Ping!"

import math
def volume(r):
    """Returns the volume of a sphere"""
    v = (4.0/3.0) * math.pi * r ** 3
    return v

def triangle_area(b, h):
    """Returns the area of  a triangle with base b and height h."""
    return 0.5 * b * h

def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters."""
    inchest_to_cm = inches * 2.54
    feeet_to_cm = feet *12 * 2.54
    return inchest_to_cm + feeet_to_cm

print(ping())
print(volume(2))
print("Are of Triangle: ", triangle_area(3, 6))
print(cm(feet = 5))
print(cm(inches = 8))
print(cm(feet = 5, inches=8))




