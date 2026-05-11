# student scorce management system , student name , course detials, unique skill. (set for unique skills,  list for skills , tuple for course,  dictionary for student details

def stu_name():
    name = input("enter student name:")
    return name

def stu_course():
    course = ("Python Programming", "T21052", 6)
    return course

def stu_skills():
    skills = ["Python", "Communication", "Teamwork", "coding "]
    return skills


def stu_unique_skills(skills):
    return set(skills)


def stu_student_details():
    course = stu_course()
    skills = stu_skills()
    unique_skills = stu_unique_skills(skills)

    student_name = input("Enter student name: ")
    roll_no_input = input("Enter roll number: ")
    score_input = input("Enter score (0-100): ")

    try:
        roll_no = int(roll_no_input)
    except ValueError:
        roll_no = 101

    try:
        score = int(score_input)
    except ValueError:
        score = 89

    student = {
        "student_name": student_name,
        "roll_no": roll_no,
        "course_details": course,
        "skills": skills,
        "unique_skills": unique_skills,
        "score": score
    }
    return student


while True:
    print("1. student name")
    print("2. course details")
    print("3. skills")
    print("4. unique skills")
    print("5. student details")
    print("6. exit")

    choice = input("enter your choice:")

    if choice == "1":
        print(stu_name())
    elif choice == "2":
        print(stu_course())
    elif choice == "3":
        print(stu_skills())
    elif choice == "4":
        skills = stu_skills()
        print(stu_unique_skills(skills))
    elif choice == "5":
        print(stu_student_details())
    elif choice == "6":
        print("exiting the program...")
        break
    else:
        print("invalid choice. please try again.")
        







