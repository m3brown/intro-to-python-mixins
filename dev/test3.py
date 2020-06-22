class LogInitMixin(object):
    def __init__(self, *args, **kwargs):
        print(f"activating {self.__class__.__name__}")
        super().__init__(*args, **kwargs)

class Student(LogInitMixin):
    pass

class Website(LogInitMixin):
    pass

Student()
Website()

# Output:
# activating Student
# activating Website
