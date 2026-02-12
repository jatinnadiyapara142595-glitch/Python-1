# 7. Menu Driven Program: Student Result
# System
# Operations:
#  Enter Marks
#  Calculate Percentage
#  Assign Grade

marks = []

def enter_marks():
    global marks
    marks = []
    for i in range(3):
        m = float(input("Enter marks of subject {}: ".format(i+1)))
        marks.append(m)

def calculate_percentage():
    if marks:
        return sum(marks) / len(marks)
    else:
        print("Enter marks first!")

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


while True:
    print("\n1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        enter_marks()
    elif choice == '2':
        per = calculate_percentage()
        if per:
            print("Percentage:", per)
    elif choice == '3':
        per = calculate_percentage()
        if per:
            print("Grade:", assign_grade(per))
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
