import math

# Find the distance from Manila and Cebu
# Ask the user to enter the coordinates of Manila
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Ask the user to enter the coordinates of Cebu
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result rounded to two decimal places
print(f"The distance between Manila and Cebu is: (distance:.2f)")