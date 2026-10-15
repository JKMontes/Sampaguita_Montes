num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
sum = 0
dif = 0

def calculate_sum():
    global num1, num2, sum
    sum = num1 + num2
    print(f"Sum: {sum}")

def calculate_difference():
    global num1, num2, dif
    dif = num1 - num2
    print(f"Difference: {dif}")

print("")
calculate_sum()
calculate_difference()