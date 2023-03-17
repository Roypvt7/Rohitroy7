import math

def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius**2

print("Area of triangle is: ",triangle_area())
print("Area of rectangle is: ",rectangle_area())
print("Area of circle is: ",circle_area())
