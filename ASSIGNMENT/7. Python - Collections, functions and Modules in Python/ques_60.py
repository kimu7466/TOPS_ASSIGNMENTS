#Q. 60  Write a Python program to calculate surface area and volume and area of a cylinder.


import math

radius = float (input("enter the radius of cylinder "))
height = float (input("enter the height of cylinder "))

surface_area = 2 * math.pi * radius * (radius + height)

volume = math.pi * radius ** 2 * height

print("The surface area of the cylinder is: ",surface_area)
print("The volume of the cylinder is: ",volume)

