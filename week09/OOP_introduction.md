# Въведение в ООП - Python
## 1. Класове
* Класът е вид абстракция, чрез която потребителя дефинира нови структури от данни от тип съответния клас. Тази нова структура се дефинира чрез ключовата дума `class`; 
* Според конвенцията името на класа започва с главна буква, а ако в него се съдържат няколко думи, е във формат `CamelCase`.

```py
class Person():
  pass
```
> _**Забележка**_: Чрез ключовата дума `pass` казваме на програмата, че ще попълним блок от команди на по-късен етап.

## 2. Обекти на класа (instance of a class)

- Всеки клас притежава обекти;
- Обектът е контейнер, характеризиращ се със състояние (state) и поведение (behaviour):
  - Под state се разбира какви данни (data) притежава всеки обект (например всеки човек има име, възраст, пол и т.н.);
  - Чрез behaviours описваме функционалността на всеки обект (например човекът може да говори, да ходи и т.н.).

- Как се създава обект?

```py
person1 = Person()
```

- Извеждане на обект в конзолата

```py
print(person1 = Person()) # <__main__.Person object at 0x000001C5939C5BE0>
```

> _**Забележка**_: <br> - Чрез създаването на обекта `person1` от тип `Person` се създава празно хранилище (storage), чието съдържание можете да проверите чрез dunder методa `__dict__`. <br> - ` <__main__.Person object at 0x000001C5939C5BE0>` представлява обекта `person1`, като в него се съдържат името на класа `Person` и адресът на обекта в паметта в шестнадесетична бройна система.

> _**Забележка**_: dunder означава double underscore, или двойна подчертавка, която слагаме в началото и в края на името на метода.

* `isinstance(obj, class)` - функция, чрез която проверяваме дали даден обект е член на даден клас
```py
print(isinstanceof(person1, Person)) # True 
```

## 3. Атрибути
### a) атрибути на обект
* Атрибутите на даден обект описват състоянието му
* Как добавяме атрибути на обектите?

```py
person1.name = "John"
print(person.name) # John
```

> _**Забележка**_: По този начин само към storage-а на обекта `person1` добавяме атрибута `name`. При създаването на следващ обект от тип `Person` (например `person2`) чрез употребата на `__dict__` метода ще установим, че неговият state не притежава атрибута `name`.

_**Решение**_: dunder метода `__init__`

  * `__init__` е специален метод, чрез който динамично се инициализира даден обект (т.е. не е нужно този метод да бъде извикан допълнително);
  * задължителен агрумент на тази член функция е ключовата дума `self`, чрез която се представлява всеки един обект от класа (person1, person2, ...).
```py
class Person:
  def __init__(self, name):
    self.name = name

person1 = Person("John")
person2 = Person("Jane")

print(person1.name) # John
print(person2.name) # Jane
```

### б) атрибути на клас
* Атрибути, достъпни за всеки един обект от класа;
* Употреба:
  * константи (атрибутът `age`)

```py
class Person:
  age = 21
  
  def __init__(self, name):
    self.name = name

person1 = Person("John")
person2 = Person("Jane")

print(person1.age) # 21
print(person2.age) # 21
```

  * променливи, съхраняващи данни за обектите (атрибутът `cnt`)
 
```py
class Person:
  cnt = 0 # count number of instances of class Person
  
  def __init__(self, name):
    self.name = name
    Person.cnt += 1

person1 = Person("John")
person2 = Person("Jane")

print(Person.cnt) # 2
```

> _**Забележка**_: Storage-а на всеки обект и storage-а на класа са **различни контейнери**! Когато въведем `person1.age`, програмата претърсва storage-а с атрибутите на `person1` и когато не открие там атрибута `age`, се качва едно ниво нагоре и търси за него в storage-a на класа `Person`.

## 4. Методи
### a) методи на обект
* Функции, които са свързани с обектите от даден клас

```py
class Person:
  def __init__(self, name):
    self.name = name
  
  def greet():
    print(f"Hello!")
 
Person.greet() # Hello!
```
По-различен резутат получаваме, когато извикаме метода чрез обекта:
```py
person1 = Person("John")
person1.greet()
```
``` py
Output[]:
TypeError: greet() takes 0 positional arguments but 1 was given
```
> _**Пояснение**_: Това се получава, тъй като чрез `person1.greet()` ние подаваме като аргумент `person1` на метода `greet()`, който не очаква от своя страна стойност, която да приеме при извикването си.

Решение: добавяне на аргумент `self` в метода:

```py
class Person:
  def __init__(self, name):
    self.name = name
  
  def greet(self):
    print(f"Hello!")
 
person1 = Person("John")
person1.greet() # Hello
```

### б) методи на клас
* Функции, който не са свързани с обектите, а само с класа;
* използва се декоратора `@classmethod`, чрез който да подскажем на програмата, че следващият метод е метод на клас;
* вместо `self` пишем `cls` като аргумент на метода;
* Употреба: за създаване на специфични обекти на класа.

```py
class Person:
  def __init__(self, name):
    self.name = name
  
  @classmethod
  def create_anonymous(cls): 
    return Person("Anonymous") # factory method - returns objects of a class

anonymous1 = Person.create_anonymous()
print(anonymous1.name) # Anonymous
```

### в) статични методи
* Функции, които не могат да достигнат и променят състоянието на обекти и класа;
* използва се декоратора `@staticmethod`;
* Употреба: за дефиниране на помощни методи или групови функции, които имат логически връзки в класа.

```py 
class Person:
  @staticmethod
  def job_title(job):
    return f"All the people here are {job}."

print(Person.job_title("developers")) # All the persons here are developers.


