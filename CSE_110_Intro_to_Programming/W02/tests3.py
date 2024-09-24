import math

lenght_square = float(input("What is the length of a side of the square? (in cm) "))
square_area = lenght_square ** 2
print(f"The area of the square is: {square_area} cm²\n")
print(f"The area of the square is: {square_area / 10000} m²\n")

lenght_rectangle = float(input("What is the length of rectangle? (in cm)"))
width_rectangle = float(input("What is the width of rectangle? (in cm)"))
rectangle_area = lenght_rectangle * width_rectangle
print(f"The area of the rectangle is: {rectangle_area} cm²\n")
print(f"The area of the rectangle is: {rectangle_area / 10000} m²")

circle_radius = float(input("\nWhat is the radius of the circle? (in cm)"))
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area} cm²\n")
print(f"The area of the circle is: {circle_area / 10000} m²")