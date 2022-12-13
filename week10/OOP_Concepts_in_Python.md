# ООП Принципи в Python
## 1. Въведение
В предишната тема разгледахме част от принципите на ООП (създаване на клас и обекти от съответния клас). Ще използваме следния програмен код като база, която ще допълваме с част от новите концепции.
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old"


p1 = Person("Amy", 23)
print(p1)
```
> Чрез метода `__repr_` връщаме подходящо съобщение при извеждане на обекта в конзолата вместо неговия адрес в ОП.

## 2. Капсулация (Encapsulation)
* начин за предпазване достъпа на дадени свойства от потребителите;
* единственият вариант, по който могат да бъдат достъпни тези данни, са чрез специални методи, наречени setter и getter (в зависимост от задачата ни).
* атрибутите могат да бъдат публични (public), защитени (_protected) и частни (__private). По конвенция публичните и защитените атрибути са дефинирани в Python без специално означение, но частните запазват своята дефиниция като атрибути, които се достъпват само в рамките на класа. 

### Пример
 Нека сега да създадем частен атрибут `__bank_account_id` в нашия клас `Person` и да имаме достъп до него само чрез новосъздадения метод `get_bank_account_id(self)`. Нека да променяме id-то чрез друг метод `set_new_bank_id`.
 
```py
 class Person:
    def __init__(self, name, age, bank_account_id):
        self.name = name
        self.age = age
        self.__bank_account_id = bank_account_id
        self.__new_bank_id = None

    def set_new_bank_id(self, new_bank_id):
        self.__new_bank_id = new_bank_id
        return "ID is changed."

    def get_bank_account_id(self):
        if self.__new_bank_id:
            self.__bank_account_id = self.__new_bank_id
        return self.__bank_account_id

    def __repr__(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old"


p1 = Person("Amy", 23, 12345)
print(p1)
print(p1.get_bank_account_id()) # 12345
print(p1.set_new_bank_id(3456))
print(p1.get_bank_account_id()) # 3456
```

## 3. Наследяване (Inheritance)
* наследяване на атрибути и методи на друг клас
* Този клас, който е наследник на друг клас, се нарича subclass или child class, а класа, от който се наследява - superclass или parent class.

### Пример
Нека създадем нов клас `BankAsisstant(Person)`, чиито обекти освен клиенти на банката са и нейни служители.

```py
class Person:
    def __init__(self, name, age, bank_account_id):
        self.name = name
        self.age = age
        self.__bank_account_id = bank_account_id
        self.__new_bank_id = None
    
    def set_new_bank_id(self, new_bank_id):
        self.__new_bank_id = new_bank_id
        return "ID is changed."

    def get_bank_account_id(self):
        if self.__new_bank_id:
            self.__bank_account_id = self.__new_bank_id
        return self.__bank_account_id

    def __repr__(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old"

class BankAsisstant(Person):
    def __init__(self, name, age, bank_account_id, assistant_id):
        super().__init__(name, age, bank_account_id)
        self.assistant_id = assitant_id
    
     def __repr__(self):
        return f"Hello, my name is {self.name}, I'm {self.age} years old and I'm a bank assistant with id {self.assistant_id}"
```
> Чрез `super().__init__(...)` класа BankAssistant наследи абсолютно всички атрибути на родителския си клас Person, като допълни своя списък от атрибути с още един - assistant_id. Наследяването на методи на даден клас се постига чрез създаване на методи със същото име в дъщерния клас и ние си задаваме какво да връща конкретната член-функция като резултат (т.е. не е задължително да е същият резултат, какъвто е в метода на родителския клас).

## 4. Полиморфизъм (Polymorphism)

* буквално значение: something that takes on multiple forms;
* на практика използваме полиморфизм при употреба на методи от родителския клас в дъщерния клас, като ги модифицираме за целите на наследяващия клас.
* методът `__repr__` в класа BankAsisstant e пример за полиморфизъм, тъй като именуваме в родителския и дъщерния клас по еднакъв начин конкретния метод, но се връщат различни резултати при принтирането на обектите от различните класове в конзолата.

## 5. Абстракция (Abstraction)

* използваме абстрация в случаите, когато искаме да скрием сложността на програмата ни от потребителя, за да може той да се фокусира върху внедряването на по-сложна логика без да мисли за кода, който стои на "заден план";
* пример от живота: употребата на социалните мрежи (чатене, пращане на изображения,...) - ние като потребители не се интересуваме от това какво стои зад изпълнението на съответните функции;
* как се реализира - чрез създаване на абстрактен клас, съдържащ абстрактни методи;
* !!!Важно за абстрактните класове - **те не създават обекти, а служат за template на своите дъщерни класове**. Трябва да **съдържат поне един абстрактен метод**, за да ги наричаме абстрактни класове!!!
* `абстрактен метод` - метод, **който се декларира, но не съдържа имплементация в себе си**, той служи за идентификатор на функционалността, която трябва да бъде реализирана от всички негови подкласове;
* всички методи трябва да бъдат пренаписани в дъщерните класове на съответния абстрактен клас;
* индикатори за абстракция в програмата: `ABC`, `@abstractmethod`.

### Пример
```py
from abc import ABC, abstractmethod # нужни при абстракция


class Shape(ABC): # ABC == Abstract Base Class - задаваме базовия клас,
    # който съдържа информацията каква обща функционалност ще има между всеки неин дъщерен клас

    @abstractmethod # property, чрез което подсказваме на програмата, че следва абстрактен метод
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


rect1 = Rectangle(10, 5)
print(rect1.area()) # 50
print(rect1.perimeter()) # 30

sq1 = Square(4)
print(sq1.area()) # 16
print(sq1.perimeter()) # 16
```
### Повече информация
* https://www.freecodecamp.org/news/object-oriented-programming-in-python/amp/?fbclid=IwAR3xyVawmtjYYdsHnzJId9i2M9ox9HZkNX1ZoyTuXjNyAi9kuhfnTj-3STs
* https://www.geeksforgeeks.org/python-oops-concepts/
* https://www.mygreatlearning.com/blog/abstraction-in-python/
