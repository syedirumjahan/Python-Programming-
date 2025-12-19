#AREA & CIRCUMFERENCE OF A CIRCLE

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print(f"Area of the circle is {area}")
print(f"Circumference of the circle is {circumference}")
