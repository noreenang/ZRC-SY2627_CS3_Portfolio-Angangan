class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = True
        self.__grade = None
        self.__submitted_files = [] 

    def __validate_grade(self, score):
        if not (0 <= score <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        return True

    def __check_submission_status(self):
        if len(self.__submitted_files) == 0:
            self.__is_submitted = False
        return self.__is_submitted

    def __is_duplicate(self, filename):
      
        if filename in self.__submitted_files:
            return False
        return True

    def add_file(self, filename):
        if self.__is_duplicate(filename) != True:
            print(f"File '{filename}' has already been submitted.")
        else:
            self.__submitted_files.append(filename)
            print(f"File '{filename}' added successfully. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename):
        if self.__grade != None:
            print(f"{self.student_name} cannot remove files. Assignement already graded.")
        elif filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"File '{filename}' removed successfully.")                    
        else:
            print(f"File '{filename}' not found in the submission.")

    def assign_grade(self, score):
        if self.__check_submission_status == True:
            if self.__validate_grade(score) == True:
                self.__grade = score
                print(f"Grade {self.__grade} assigned to {self.student_name}") 
        else:
            print("Cannot grade. No submision found.")
        

    def get_grade(self):
        return self.__grade

    def view_files(self):
        return self.__submitted_files

    def get_status_report(self):
        status = "Submitted" if self.__check_submission_status() else "Not Submitted"
        return {
            "Student Name": self.student_name,
            "Student ID": self.student_id,
            "Assignment Title": self._assignment_title,
            "Due Date": self._due_date,
            "Submission Status": status,
            "Grade": self.__grade,
            "Submitted Files": self.__submitted_files
        }

student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date=" 2026-10-01")
student3 = AssignmentSubmission (student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date=" 2026-10-0")
student5 = AssignmentSubmission (student_name="Jose Reyes", student_id="pshs-1055-X", assignment_title="CS-101", due_date="2026-10-01")

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files---")
student3.add_file("script.py")
student3.add_file("script.py") # Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded -=-")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf") # Blocked by grading status
print()

print("--- TEST SCENARIO 5: Empty List Handling ----")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) # Should fail because list is empty print ()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
