class mca:
    def __init__(self,name,rollno,section):
        self.name = name
        self.rollno = rollno
        self.section = section
    def display_students(self):
        print("Student name :{}".format(self.name))
        print("Student roll number :{}".format(self.rollno))
        print("Section :{}".format(self.section))

class student(mca):
    def __init__(self,name,rollno,section,admission):
        super().__init__(name,rollno,section)
        self.admission_number = admission

    def display_students(self):
        super().display_students()
        print("admisson number : {}".format(self.admission_number))

student1 =student("chandra sekhar", "215N1F0025","A section",2001)
student1.display_students()