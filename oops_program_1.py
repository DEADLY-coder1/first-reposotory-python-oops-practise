class mca:
    def __init__(self,name,rollno,section):
        self.name = name
        self.rollno = rollno
        self.section = section
    def display_students(self):
        print("Student name :{}".format(self.name))
        print("Student roll number :{}".format(self.rollno))
        print("Section :{}".format(self.section))


student1 =mca("chandra sekhar", "215N1F0025","A section")
student1.display_students()