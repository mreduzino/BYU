import math

side = float(input("What is the length of a side of the square? "))
square_area = side ** 2
print(f"The area of the square is: {square_area:.2f}")

rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of rectangle? "))
rectangle_area = rectangle_length*rectangle_width
print(f"The area of the rectangle is: {rectangle_area:.2f}")

circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area:.2f}")

'''

#Stretch challenges#

single_value = float(input("Enter a single a value: "))
square_single_value_area = single_value ** 2
circle_single_value_area = math.pi * (single_value ** 2)
cube_volume = single_value ** 3
sphere_volume = (4 / 3) * math.pi * (single_value ** 3)
print(f"The area of the square is: {square_single_value_area:2.2f}")
print(f"The area of the circle is: {circle_single_value_area:2.2f}")
print(f"The volume of the cube is: {cube_volume:2.2f}")
print(f"The volume of the sphere is: {sphere_volume:2.2f}")


#Stretch challenge 3#
side = float(input("What is the length of a side of the square? (in cm): "))
square_area = side ** 2
square_area_m = square_area / 100
print(f"The area of the square in CM is: {square_area:.2f}CM²")
print(f"The area of the square in M is: {square_area_m:2.2f}M²")

rectangle_length = float(input("What is the length of rectangle? in cm: "))
rectangle_width = float(input("What is the width of rectangle? in cm: "))
rectangle_area = rectangle_length*rectangle_width
rectangle_area_m = rectangle_area / 100
print(f"The area of the rectangle in CM is: {rectangle_area:.2f}CM²")
print(f"The area of the rectangle in M is: {rectangle_area_m:2.2f}M²")

circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * (circle_radius ** 2)
circle_area_m = circle_area / 100
print(f"The area of the circle in CM is: {circle_area:.2f}CM²")
print(f"The area of the circle in M is: {circle_area_m:2.2f}M²")

'''