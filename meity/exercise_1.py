class Student:
 def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks
 def display(self):
    print("Name:", self.name)
    print("Roll No:", self.roll_no)
    print("Marks:", self.marks)
 def calculate_percentage(self):
    return (self.marks / 100) * 100
class GraduateStudent(Student):
 def __init__(self, name, roll_no, marks, degree_program):
    super().__init__(name, roll_no, marks)
    self.degree_program = degree_program
 def assign_grade(self):
    if self.marks >= 90:
        return 'A'
    elif self.marks >= 80:
        return 'B'
    elif self.marks >= 70:
        return 'C'
    elif self.marks >= 60:
        return 'D'
    else:
        return 'F'
 def display(self):
    super().display()
    print("Degree Program:", self.degree_program)
    print("Grade:", self.assign_grade())
def main():
 name = input("Enter student's name: ")
 roll_no = int(input("Enter student's roll number: "))
 marks = int(input("Enter student's marks (out of 100): "))
 student = Student(name, roll_no, marks)
 student.display()
 print("Percentage:", student.calculate_percentage())
 degree_program = input("Enter graduate student's degree program: ")
 grad_student = GraduateStudent(name, roll_no, marks, degree_program)
 grad_student.display()
if __name__ == "__main__":
 main()