import math

def compute_area_square(side):
    return side * side
def compute_area_rectangle(length, width):
    return length * width
def compute_area_circle(radius):
    return 2 * math.pi * radius

shape = input("What kind of shape do you have? (square, rectangle, circle, or type quit) ")

while shape != "quit":
    if shape == "square":
        side = float(input("What is the side length? "))
        print(f"The area of the square is: {compute_area_square(side)}")
        break
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        print(f"The area of the rectangle is: {compute_area_rectangle(length, width)}")
        break
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        print(f"The area of the circle is: {compute_area_circle(radius)}")
        break
    else:
        print("Invalid shape")
        break