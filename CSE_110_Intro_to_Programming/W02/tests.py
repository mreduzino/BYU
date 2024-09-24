import math

lenght_square = float(input("What is the length of a side of the square? "))
square_area = lenght_square ** 2
print(f"The area of the square is: {square_area:.1f}")

lenght_rectangle = float(input("\nWhat is the length of rectangle? "))
width_rectangle = float(input("What is the width of rectangle? "))
rectangle_area = lenght_rectangle * width_rectangle
print(f"The area of the rectangle is: {rectangle_area:.1f}")

circle_radius = float(input("\nWhat is the radius of the circle? "))
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area:.1f}")