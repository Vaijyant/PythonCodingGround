import math

def area(r):
    """Area of a circle with radius 'r'"""
    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

# Method 2: Use 'map' functions
print(list(map(area, radii)))

print("===========")


temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
        ("Los Angeles", 26), ("Tokyo", 27),
        ("New York", 28), ("London", 22), ("Beiking", 32)]


c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temps)))

print("===========")

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

print(list(filter(lambda x: x > avg, data)))

print("===========")

countries = ["", "Argentina", "Brazil", "Chile", 
            "", "Colombia", "", "Ecuador", "", "",
            "Venezuela"]

print(list(filter(None, countries)))


print("===========")

from functools import reduce
# Multiply all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y
print(reduce(multi, data))



