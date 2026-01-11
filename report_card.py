# Student Report Card Generator

def calculate_grade(percentage):
    """Calculate grade based on percentage"""
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def get_marks(subjects):
    """Get marks for all subjects with validation"""
    marks = {}
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")
    return marks

def generate_report_card():
    """Generate the student's report card"""
    print("=== Student Report Card Generator ===")
    
    # Student information
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    class_name = input("Enter class/grade: ")
    
    # Subjects
    subjects = ['Math', 'Science', 'English', 'History', 'Computer']
    
    # Get marks
    marks = get_marks(subjects)
    
    # Calculations
    total = sum(marks.values())
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)
    
    # Display report card
    print("\n" + "="*30)
    print(f"Report Card for {name}")
    print(f"Roll No: {roll_no}")
    print(f"Class: {class_name}")
    print("="*30)
    
    for subject, score in marks.items():
        print(f"{subject}: {score}")
    
    print("="*30)
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("="*30)

# Run the program
generate_report_card()
