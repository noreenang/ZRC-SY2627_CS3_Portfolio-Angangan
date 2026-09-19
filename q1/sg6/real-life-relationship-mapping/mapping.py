class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.student_id})"


class Course:
    def __init__(self, course_code: str, course_name: str):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []  

    def add_student(self, student: Student) -> None:
        """Appends a Student object to the course's student list."""
        self.students.append(student)
        print(f"Added {student.name} to {self.course_code}.")

    def display_enrolled_students(self) -> None:
        """Displays all students currently in the course."""
        print(f"\n--- Enrolled Students in {self.course_code}: {self.course_name} ---")
        if not self.students:
            print("No students enrolled yet.")
        else:
            for student in self.students:
                print(f"- {student}")



if __name__ == "__main__":
 
    cs101 = Course("CS101", "Introduction to Computer Science")

    student1 = Student("S101", "Alice Smith")
    student2 = Student("S102", "Bob Jones")

    cs101.add_student(student1)
    cs101.add_student(student2)

    cs101.display_enrolled_students()
