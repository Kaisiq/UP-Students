# Решение на ООП задача

Следното решение създава клас `Student`, проверява въведените данни, подрежда студентите по успех и извежда студентите с най-нисък и най-висок успех.

```py
class Student:
    def __init__(self, name, uspeh):
        self.name = name
        self.uspeh = uspeh

    @staticmethod
    def isValidName(name):
        return len(name) <= 30

    @staticmethod
    def isValidUspeh(uspeh):
        return 2 <= uspeh <= 6

    def print(self):
        print(self.name, self.uspeh)


def generateListOfStudents(n):
    lst = []
    for _ in range(n):
        newName = input()
        while not Student.isValidName(newName):
            newName = input()

        newUspeh = float(input())
        while not Student.isValidUspeh(newUspeh):
            newUspeh = float(input())

        lst.append(Student(newName, newUspeh))

    lst.sort(key=lambda x: x.uspeh)
    lst[0].print()
    lst[-1].print()


n = int(input())
generateListOfStudents(n)
```
