#Validating Data Input and Verifying Output

#1. Payment Method Checker
#Ask the user for the payment method
vp = ["GCash", "Cash", "Card"]

#Validate the payment and show the output
payment = input("Enter payment method: ")
if payment in vp:
    print("Valid payment method.")
else:
    print("Invalid payment method.")

#2. Grade Checker
#Ask the user to enter a grade
grade = int(input("Enter your grade: "))

#Validate the grade and show output
if 0 <= grade <= 100:
    print("Valid grade.")
else:
    print("Invalid grade. Grade must be between 0 and 100.")

#3. Student ID Checker
#Ask the user to enter a Student ID in the specific format
import re

sID = input("Enter student ID: ")
pattern = r"\d{4}-\d{4}"

#Validate the ID and show output
if re.fullmatch(pattern, sID):
    print("Valid student ID.")
else:
    print("Invalid student ID.")

#4. PIN Validator
#Ask the user to create a PIN.
pin = input("Create a 6-digit PIN:")

#Validate PIN and show output
if len(pin) == 6 and pin.isdigit():
    print("Valid PIN.")
else:
    print("Invalid PIN. Enter exactly 6 digits.")

#5. Student Score Entry
#Ask the user to enter an examination score
try:
    ES = int(input("Enter examination score: "))

except ValueError:
    print("Invalid score. Please enter a number.")

#Validate score and show output
if ES <= 0 <= 100:
    print("Valid score.")
else:
    print("Invalid score. Score must be between 0 and 100.")


