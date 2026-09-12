class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"Student ID   : {self.student_id}")
        print(f"Student Name : {self.name}")
        print()


# ============================================================
# STUDENT DATA
# ============================================================

students = []


# ============================================================
# LOAD STUDENTS FROM TXT FILE
# ============================================================

def load_students():
    try:
        with open('student.txt', 'r') as file:

            for line in file:
                line = line.strip()

                if line:
                    student_id, name = line.split(',', 1)

                    student = Student(int(student_id), name)
                    students.append(student)

    except FileNotFoundError:
        # Create the file if it does not exist
        open('student.txt', 'w').close()

# ============================================================
# QUESTION CLASS
# ============================================================

class Question:
    def __init__(self, q_id, question, options, answer, subject):
        self.q_id = q_id
        self.question = question
        self.options = options
        self.answer = answer
        self.subject = subject

    def display(self):
        print(f"\nQuestion {self.q_id}: {self.question}")

        for key, value in self.options.items():
            print(f"{key}. {value}")


# ============================================================
# QUESTION BANK
# ============================================================

questions = [

    Question(
        1,
        "Which keyword is used to define a function in Python?",
        {
            'A': 'FUNC',
            'B': 'def',
            'C': 'FUNCTION',
            'D': 'define'
        },
        'B',
        'PYTHON'
    ),

    Question(
        2,
        "Which keyword is used to create a class in Python?",
        {
            'A': 'class',
            'B': 'object',
            'C': 'define',
            'D': 'create'
        },
        'A',
        'PYTHON'
    ),

    Question(
        3,
        "Which data type is mutable in Python?",
        {
            'A': 'Tuple',
            'B': 'String',
            'C': 'List',
            'D': 'Integer'
        },
        'C',
        'PYTHON'
    ),

    Question(
        4,
        "Which symbol is used to create a comment in Python?",
        {
            'A': '//',
            'B': '/*',
            'C': '#',
            'D': '--'
        },
        'C',
        'PYTHON'
    ),

    Question(
        5,
        "Which function is used to find the length of a list in Python?",
        {
            'A': 'count()',
            'B': 'length()',
            'C': 'size()',
            'D': 'len()'
        },
        'D',
        'PYTHON'
    ),

    Question(
        6,
        "Find the next number in the series: 2, 6, 12, 20, 30, ?",
        {
            'A': '40',
            'B': '42',
            'C': '44',
            'D': '46'
        },
        'B',
        'APTITUDE'
    ),

    Question(
        7,
        "If CAT is coded as DBU, how is DOG coded using the same pattern?",
        {
            'A': 'EPH',
            'B': 'EOG',
            'C': 'FPH',
            'D': 'DPH'
        },
        'A',
        'APTITUDE'
    ),

    Question(
        8,
        "Pointing to a man, Ravi said, "
        "\"He is the son of my mother's only son.\" "
        "How is the man related to Ravi?",
        {
            'A': 'Brother',
            'B': 'Father',
            'C': 'Son',
            'D': 'Uncle'
        },
        'C',
        'APTITUDE'
    ),

    Question(
        9,
        "A person walks 5 km north, then turns right and walks 3 km. "
        "In which direction is he from his starting point?",
        {
            'A': 'North-East',
            'B': 'North-West',
            'C': 'South-East',
            'D': 'South-West'
        },
        'A',
        'APTITUDE'
    ),

    Question(
        10,
        "Find the odd one out?",
        {
            'A': 'Triangle',
            'B': 'Square',
            'C': 'Circle',
            'D': 'Rectangle'
        },
        'C',
        'APTITUDE'
    ),

    Question(
        11,
        "Which OOP concept is used to restrict direct access to an object's data?",
        {
            'A': 'Inheritance',
            'B': 'Polymorphism',
            'C': 'Encapsulation',
            'D': 'Abstraction'
        },
        'C',
        'OOP'
    ),

    Question(
        12,
        "Which type of inheritance occurs when one child class "
        "inherits from one parent class?",
        {
            'A': 'Multiple inheritance',
            'B': 'Single inheritance',
            'C': 'Multilevel inheritance',
            'D': 'Hierarchical inheritance'
        },
        'B',
        'OOP'
    ),

    Question(
        13,
        "What is method overriding in Python?",
        {
            'A': 'Defining multiple classes with the same name',
            'B': 'Defining a method in a child class with the same name '
                 'as the parent class method',
            'C': 'Calling a method without creating an object',
            'D': 'Deleting a method from the parent class'
        },
        'B',
        'OOP'
    ),

    Question(
        14,
        "Which module is commonly used to create abstract base classes in Python?",
        {
            'A': 'random',
            'B': 'math',
            'C': 'abc',
            'D': 'os'
        },
        'C',
        'OOP'
    ),

    Question(
        15,
        "Which OOP concept allows the same method name to behave "
        "differently for different objects?",
        {
            'A': 'Encapsulation',
            'B': 'Inheritance',
            'C': 'Abstraction',
            'D': 'Polymorphism'
        },
        'D',
        'OOP'
    )
]

# ============================================================
# REGISTER STUDENT
# ============================================================

def register_student():
    ids = []
    
    for student in students:
        ids.append(student.student_id)

    old_id = max(ids)
    new_id = old_id + 1

    
    student_name =input('Enter the name:').strip().upper()
    
    if not student_name.isalpha():
        print('Name Must Be In Letters')
        return (register_student())
    
    new_student = Student(new_id,student_name)

    students.append(new_student)

    with open('student.txt', 'a') as file:
        file.write(f'\n{new_id},{student_name}')

    print('\nEnrollment successful!')
    print(f'Your student ID: {new_id}')
    print(f'Your student name: {student_name}')
#=================================================================
# STUDENT LOGIN
# ============================================================
def authenticate_student():

    try:
        student_id = int(input("Enter your ID: "))

    except ValueError:
        print("ID must be an integer.")
        return (authenticate_student())

    student_name = input("Enter your name: ").strip().upper()

    for student in students:

        if student_id == student.student_id and student_name == student.name:

            print(f"\nAccess Granted!")
            print(f"Welcome {student_name}")

            return student

    print("\nAccess Denied!")
    print("Student record not found.")

    return None

    


# ============================================================
# SELECT SUBJECT
# ============================================================

def select_subject(student):

    print("\n================================")
    print("        SELECT SUBJECT")
    print("================================")
    print("1. PYTHON")
    print("2. APTITUDE")
    print("3. OOPS")

    while True:

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number from 1-3.")
            continue

        if choice == 1:
            subject = 'PYTHON'
            break

        elif choice == 2:
            subject = 'APTITUDE'
            break

        elif choice == 3:
            subject = 'OOP'
            break

        else:
            print("Invalid choice. Please select 1-3.")

    attempt_exam(subject, student)


# ============================================================
# ATTEMPT EXAM
# ============================================================

def attempt_exam(subject, student):

    score = 0
    correct = 0
    incorrect = 0
    unanswered = 0
    total = 0

    print("\n********************************")
    print(f"        {subject} EXAM")
    print("********************************")

    for question in questions:

        if question.subject == subject:

            total += 1

            question.display()

            user_answer = input(
                "Enter your answer (A/B/C/D): "
            ).strip().upper()

            # -----------------------------------------
            # UNANSWERED
            # -----------------------------------------

            if user_answer == '':
                print("Question not attempted.")
                unanswered += 1

            # -----------------------------------------
            # CORRECT ANSWER
            # -----------------------------------------

            elif user_answer == question.answer:
                print("Correct answer!")
                correct += 1
                score += 1

            # -----------------------------------------
            # INCORRECT ANSWER
            # -----------------------------------------

            else:
                print(
                    f"Wrong answer! "
                    f"Correct answer is {question.answer}"
                )
                incorrect += 1

    # Send all evaluation details to result module
    generate_result(
        student,
        subject,
        total,
        correct,
        incorrect,
        unanswered,
        score
    )


# ============================================================
# GENERATE RESULT
# ============================================================

def generate_result(
    student,
    subject,
    total,
    correct,
    incorrect,
    unanswered,
    score
):

    if total > 0:
        percentage = (score / total) * 100
    else:
        percentage = 0

    # Result stored in dictionary
    result = {
        'Student ID': student.student_id,
        'Student Name': student.name,
        'Subject': subject,
        'Total Questions': total,
        'Correct Answers': correct,
        'Incorrect Answers': incorrect,
        'Unanswered': unanswered,
        'Score': score,
        'Percentage': percentage
    }

    display_result(result)
    save_result(result)


# ============================================================
# DISPLAY RESULT
# ============================================================

def display_result(result):

    print("\n********************************")
    print("          EXAM RESULT")
    print("********************************")

    print(f"Student ID       : {result['Student ID']}")
    print(f"Student Name     : {result['Student Name']}")
    print(f"Subject          : {result['Subject']}")
    print(f"Total Questions  : {result['Total Questions']}")
    print(f"Correct Answers  : {result['Correct Answers']}")
    print(f"Incorrect Answers: {result['Incorrect Answers']}")
    print(f"Unanswered       : {result['Unanswered']}")
    print(f"Score            : {result['Score']}")
    print(f"Percentage       : {result['Percentage']:.2f}%")

    print("********************************")


# ============================================================
# SAVE RESULT TO TXT FILE
# ============================================================

def save_result(result):

    try:

        with open('results.txt', 'a') as file:

            file.write("------------------------------\n")
            file.write(f"Student ID: {result['Student ID']}\n")
            file.write(f"Student Name: {result['Student Name']}\n")
            file.write(f"Subject: {result['Subject']}\n")
            file.write(
                f"Total Questions: "
                f"{result['Total Questions']}\n"
            )
            file.write(
                f"Correct Answers: "
                f"{result['Correct Answers']}\n"
            )
            file.write(
                f"Incorrect Answers: "
                f"{result['Incorrect Answers']}\n"
            )
            file.write(
                f"Unanswered: "
                f"{result['Unanswered']}\n"
            )
            file.write(
                f"Score: "
                f"{result['Score']}\n"
            )
            file.write(
                f"Percentage: "
                f"{result['Percentage']:.2f}%\n"
            )
            file.write("------------------------------\n\n")

        print("\nResult saved successfully!")

    except Exception:
        print("\nError while saving result.")


# ============================================================
# VIEW STUDENT RESULT
# ============================================================

def view_result():

    try:
         student_id = int(input("Enter your Student ID: "))

    except ValueError:
        print("Student ID must be a number.")
        return

    try:
        with open('results.txt', 'r') as file:

            result_found = False
            lines = file.readlines()

            for i in range(len(lines)):

                if lines[i].startswith("Student ID:"):

                    saved_id = int(lines[i].split(":")[1].strip())

                    if saved_id == student_id:

                        result_found = True

                        print("\n********************************")
                        print("          EXAM RESULT")
                        print("********************************")

                        # Print this complete result
                        for j in range(i, min(i + 10, len(lines))):
                            print(lines[j], end="")

                        print("********************************")

            if not result_found:
                print("\nNo result found for this Student ID.")

    except FileNotFoundError:
        print("\nNo results available yet.")       


# ============================================================
# MAIN PROGRAM
# ============================================================

load_students()

while True:

    print("\n================================")
    print("       STUDENT EXAM SYSTEM")
    print("================================")
    print("1. ENROLLMENT")
    print("2. LOGIN")
    print("3. VIEW RESULTS")
    print("4. VIEW ALL STUDENTS")
    print("5. EXIT")

    try:
        choice = int(input("Select an option (1-4): "))

    except ValueError:
        print("The option should be a number.")
        continue

    # -----------------------------------------
    # REGISTER
    # -----------------------------------------

    if choice == 1:
        register_student()

    # -----------------------------------------
    # LOGIN
    # -----------------------------------------

    elif choice == 2:

        student = authenticate_student()

        if student:
            select_subject(student)
    # ----------------------------------------
    #RESULTS
    #-----------------------------------------

    elif choice == 3:
        view_result()

        
    # -----------------------------------------
    # VIEW STUDENTS
    # -----------------------------------------

    elif choice == 4:

        if len(students) == 0:
            print("No students registered.")

        else:
            print("\n========== STUDENT LIST ==========")

            for student in students:
                student.display()

    # -----------------------------------------
    # EXIT
    # -----------------------------------------

    elif choice == 5:
        print("\nExiting System...")
        break

    else:
        print("Enter a number from 1-4.")
