class Student():

    def __init__(self, name, uspeh):
        self.name = name
        self.uspeh = uspeh

    @staticmethod
    def isValidName(name):
        return(len(name) <= 30)

    @staticmethod
    def isValidUspeh(uspeh):
        return(uspeh >= 2 and uspeh <= 6)

    def print(self):
        print(self.name, self.uspeh)


def generateListOfStudents(n):
    lst = []

    for i in range(0,n):

        newName = input()
        while( not (Student.isValidName(newName) ) ):
            newName = input()

        newUspeh = float(input())
        while( not (Student.isValidUspeh(newUspeh))):
            newUspeh = float(input())

        student1 = Student(newName, newUspeh)
        lst.append(student1)

    lst.sort(key= lambda x : x.uspeh)
    lst[0].print()
    length = len(lst)
    lst[length-1].print()

n = int(input())
generateListOfStudents(n)