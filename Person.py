class Person():

    name = ""
    age = 0

    def  __init__(self , person_name,person_age, ):
        self.age  = person_age
        self.name = person_name

    def __repr__(self):
        return('Peron name \t{} and age\t{}'.format( self.name , self.age))

class Student( Person):

    studentId = ""
    def __init__(self, student_name, student_age,student_id):

        Person.__init__(student_name, student_age)
        self.studentId =student_id
n


p1 = Person('Niran' , 36)
print(p1)