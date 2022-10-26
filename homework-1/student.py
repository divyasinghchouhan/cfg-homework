
"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


class CFGStudent(Student):
    def __init__(self, name, age, id, specialisation):
        super().__init__(name, age, id)
        self.specialisation = specialisation.capitalize()
        self.subject = set()
        self.average = None

    def view_student_details(self):
        print(f"\n–––––––––––––––\n"
              f"STUDENT DETAILS\n"
              f"–––––––––––––––\n"
              f"Student Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Student ID: {self.id}\n"
              f"Specialisation: {self.specialisation}\n"
              f"Subjects: {self.subjects}\n"
              f"Average: {self.average}\n")


    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        del self.subjects[subject]
        print(f"{self.name} is no longer registered on "
              f"{subject}.")

    def view_subject(self):
        for subject in self.subjects.keys():
            print(subject)

    def average_marks(self):
        average = 0
        num = 0
        for marks in self.subjects.values():
            average += int(marks)
            num += 1
        average /= num
        self.average = round(average,2)
        #print("\nThe average marks of the student is", average)
        print(f"Average: {(average)}")

if __name__ == '__main__':
    student1 = CFGStudent("ABC", 20, 1, 'Software')
    student1.add_subject("Python", 90)
    student1.add_subject("SQL", 86)
    student1.add_subject("JAVA", 94)
    student1.add_subject("C++", 85)
    print("\nSubject List of specialization in software:")
    student1.view_subject()
    print("\nNew Subject List:")
    student1.remove_subject("JAVA")
    student1.view_subject()
    student1.average_marks()
    student1.view_student_details()

    student2 = CFGStudent("XYZ", 18, 2, 'Data Science')
    student2.add_subject("Python", 91)
    student2.add_subject("Machine Learning", 86)
    student2.add_subject("Statistics", 94)
    print("\nSubject List of specialization in Data Science:")
    student2.view_subject()
    student2.average_marks()
    student2.view_student_details()