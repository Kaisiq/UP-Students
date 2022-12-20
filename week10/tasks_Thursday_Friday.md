## Задачи

Създайте абстрактен клас `Triangle`, който съдържа следните характеристики и свойства:
* атрибути `a`, `b`, `c`, които отговарят на страните на триъгълника;
* статичен метод `isValid(side_a, side_b, side_c)`, който проверява дали съществува триъгълник със зададените страни;
* статичен метод `triangleType(side_a, side_b, side_c)`, в който се извършва проверката за съществуването на триъгълника и **ако такъв има**, се проверява от кой тип триъгълник е, и се създава обект от дъщерните класове на `Triangle` - `Acute`, `Right` или `Obtuse` (остроъгълен, прав, тъпоъгълен);
* абстрактните методи `area()`, `perimeter()` и `heightLen()`, които пресмятат съответно _лицето, периметъра и дължините на височините към всяка страна в конкретния тръгълник_.

> Note: Да се конструират всички методи в дъщерните класове с коректните алгоритми за пресмятане на лицето, периметъра и дължините на височините към всяка страна, изучавани в училище.

### Примерно решение (шаблон):
```py
from abc import ABC, abstractmethod
 
class Triangle():
    a = 0
    b = 0
    c = 0
 
    @staticmethod
    def isValid(side_a, side_b, side_c):
        return True
 
    @staticmethod
    def isRightTriangle(a,b,c):
        return True
 
    @staticmethod
    def isAcuteTriangle(a, b, c):
        return True
 
    @staticmethod
    def triangleType(side_a, side_b, side_c):
        if( Triangle.isValid(side_a, side_b, side_c) ):
            if(Triangle.isRightTriangle(side_a, side_b, side_c)):
                return RightTriangle(side_a, side_b, side_c)
            elif(Triangle.isAcuteTriangle(side_a,side_b,side_c)):
                pass#return AcuteTriangle(side_a, side_b, side_c)
            else:
                pass
 
        else:
            print("nevaliden vhod")
 
class RightTriangle(Triangle):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
 
 
triangle1 = Triangle.triangleType(3,4,5)
print(type(triangle1))

```
