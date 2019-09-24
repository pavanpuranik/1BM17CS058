class Student:
    def __init__(self,age,marks,idnumber):
        self.age=age
        self.marks=marks
        self.idnumber=idnumber

    def validate_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True
        else:
            return False

    def validate_age(self):
        if(self.age>20):
            return True

        else:
            return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.marks>=65:
                return True
            else:
                return False

        else:
            return False


s=Student(17,77,90)
print(s.validate_marks())
print(s.validate_age())
print(s.check_qualification())

