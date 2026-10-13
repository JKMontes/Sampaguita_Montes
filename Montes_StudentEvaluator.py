name = input("Enter student name: ")

def display_header():
    header = ("STUDENT PERFORMANCE EVALUATOR")

def get_student_info():
    A1 = float(input("Enter Assessment 1: "))
    A2 = float(input("Enter Assessment 2: "))
    A3 = float(input("Enter Assessment 3: "))

def evaluate_performance():
    average = (A1 + A2 + A3) / 3
    if 90 <= average <= 100:
        print("Outstanding")
    elif 85 <= average <= 89:
        print("Very Satisfactory")
    elif 80 <= average <= 84:
        print("Satisfactory")
    elif 75 <= average <= 79:
        print("Fairly Satisfactory")
    else:
        print("Needs Improvement")

def display_report():
    print("=" * 50)
    print(f"{header}")
    print("=" * 50)
    print(f"Student Name: {name}")
    print("")
    print(f"Assessment Scores: {A1}, {A2}, {A3}")
    print("")
    print(f"Average Score: {average}")
    print("")
    print(f"Performance Level: {evaluate_performance()}")

# JHORCEL K. MONTES
# 8 SAMPAGUITA