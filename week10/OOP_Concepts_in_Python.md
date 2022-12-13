# ООП Принципи в Python
## 1. Въведение
В предишната тема разгледахме част от принципите на ООП (създаване на клас и обекти от съответния клас). Ще използваме следния програмен код като база, която ще допълваме с новите концепции.
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
Нека създадем нов клас `BankAsisstant(Person)`, който освен клиент на банката е и нейн служител.

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
* методът `__repr__` в класа BankAsisstant e пример за полиморфизъм.











