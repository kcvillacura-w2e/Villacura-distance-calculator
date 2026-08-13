
# Distance Calculator

**Goal:** Find the distance between Manila and Cebu

**Requirements:** The coordinates of both Manila and Cebu

**Question:** What is the coordinates of both Manila and Cebu?

Look for:
- The x coordinate of Manila
- The y coordinate of Manila
- The x coordinate of Cebu
- The y coordinate of Cebu

## Step 1: Enter the coordinates of Manila
  
x1 = float(input("Enter x1: "))

y1 = float(input("Enter y1: "))

## Step 2: Enter the coordinates of Cebu

x2 = float(input("Enter x2: "))

y2 = float(input("Enter y2: "))

## Step 3: Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

## Step 4: Display the result rounded to two decimal places
print(f"The distance between Manila and Cebu is: {distance:.2f}")
