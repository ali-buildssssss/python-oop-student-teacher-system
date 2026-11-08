# python-oop-student-teacher-system

Student & Teacher Management System (Python OOP)

A small command-line project I built to practice Object-Oriented Programming in Python. It manages students and teachers, lets you add marks, and calculates grades, all from a simple text menu.

What it does
Shows a list of all students with their info, marks, department, average and grade
Shows a list of all teachers with their subject
Adds marks for students
Calculates the average and letter grade for each student
Handles wrong input (like text or decimals) without crashing
OOP concepts used
Concept	Where it shows up
Classes & objects	user, student, teacher
Inheritance	student and teacher both inherit from user using super().__init__()
Encapsulation	A student's marks are stored in a private attribute (__marks) and accessed through get_marks()
Method reuse	show_student_info() and teacher_info() reuse the parent's show_info()
Variable arguments	add_marks(*marks) accepts any number of marks at once
Error handling	try/except around the menu input
Project structure
user            -> name, age, user_id, show_info()
 ├── student    -> department, private marks, add_marks(), calculate_grade()
 └── teacher    -> subject, teacher_info()
How to run
Make sure Python 3 is installed.
Save the code as main.py.
Run it:
bash
python main.py
Menu options
1 -> students list
2 -> teacher list
3 -> add marks
4 -> grade
5 -> quit
Sample data

The program starts with three students (Ali, Usama, Zain) and two teachers (Haider, Usman) already created, so you can try everything straight away.

Grading scale
Average	Grade
90+	A+
80+	A
70+	B
60+	C
50+	D
40+ E
Below 40	F
Ideas for improvement
Let the user type in their own marks instead of fixed values
Add new students and teachers from the menu
### Author
M.Ali Ibrahim
