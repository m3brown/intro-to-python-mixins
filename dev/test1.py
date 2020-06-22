class Student:
    def print_label(self):
        print("I am a student")

class Faculty:
    def print_label(self):
        print("I am faculty")
        super().print_label()

class TA(Faculty, Student):

    def print_label(self):
        print("I am a TA!")
        super().print_label()

TA().print_label()

# Output:
# I am a TA!
# I am faculty
# I am a student
