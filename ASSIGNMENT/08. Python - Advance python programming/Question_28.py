# 28. What relationship is appropriate for Course and Faculty? 

class Course:
    def info(self, student_name, course_name):
        print(f"Course: {course_name}, Student: {student_name}")

class Faculty(Course):
    def detail(self, faculty_name, branch):
        print(f"Faculty: {faculty_name}, Branch: {branch}")

d = Faculty()

student_name = input("Enter student's name: ")
course_name = input("Enter course name: ")
faculty_name = input("Enter faculty's name: ")
branch = input("Enter branch: ")

d.info(student_name, course_name)
d.detail(faculty_name, branch)
