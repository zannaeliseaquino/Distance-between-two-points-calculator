import math

# Ask the user to enter the coordinates of the first point
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))

# Ask the user to enter the coordinates of the second point
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result rounded to two decimal places
print(f"The distance between the two points is: {distance:.2f}")
