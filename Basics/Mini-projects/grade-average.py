subjects = int(input("How many subjects: "))

all_averages = 0

for i in range(subjects):
    total = 0

    subject_name = input("\nSubject name: ")
    grades = int(input("How many grades: "))

    for j in range(grades):
        grade = float(input("Enter grade: "))
        total += grade

    average = total / grades
    all_averages += average

    print("Average for", subject_name, ":", average)

print("\nAverage of all subjects:",
      all_averages / subjects)