import math

single_lenght = float(input("Give a single length value: "))

square_area = single_lenght ** 2
print(f"The area of the square is: {square_area:.1f}")
circle_area = math.pi * (single_lenght ** 2)
print(f"The area of the circle is: {circle_area:.1f}")
cube_volume = single_lenght ** 3
print(f"The volume of the cube is: {cube_volume:.1f}")
sphere_volume = (4 / 3) * math.pi * (single_lenght ** 3)
print(f"The volume of the sphere is: {sphere_volume:.1f}")