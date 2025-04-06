import math

class Shape:
    def area(self, *args):
        if len(args) == 1:
            # Calculate area of a square
            side = args[0]
            return side * side
        elif len(args) == 2:
            # Calculate area of a rectangle
            length, width = args[0], args[1]
            return length * width
        elif len(args) == 3 and args[0] == 'circle':
            # Calculate area of a circle
            radius = args[1]
            return math.pi * radius * radius
        else:
            return "Invalid arguments"

# Example usage
shape = Shape()
print("Area of square (side=4):", shape.area(4))
print("Area of rectangle (length=4, width=5):", shape.area(4, 5))
print("Area of circle (radius=3):", shape.area( 3))