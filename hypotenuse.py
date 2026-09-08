import math

a = int(input("Input the length side of a: "))
b = int(input("Input the length side of b: "))

a2 = math.pow(a,2)
b2 = math.pow(b,2)

ab = (a2 + b2)
h = math.sqrt(ab)

print(f"The hypotenuse is:{h:.2f}")