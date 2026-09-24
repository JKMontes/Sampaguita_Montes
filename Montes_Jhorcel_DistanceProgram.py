import math

#Ask the user to enter the following variables
x1 = (int(input("Enter x1: ")))
y1 = (int(input("Enter y1: ")))
x2 = (int(input("Enter x2: ")))
y2 = (int(input("Enter y2: ")))
print("=" * 50)

#Calculate the distance using math.sqrt
XD = x2 - x1
YD = y2 - y1
XX = pow(XD, 2)
YY = pow(YD, 2)
XY = XX + YY
SQRT = math.sqrt(XY)

#Print the output/final distance
print(f"The distance between the two points is: {SQRT:.2f}")