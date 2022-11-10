# Речници

### Речниците се използват за съхраняване на голям брой данни в една променлива<br> Елементите в речниците са подредени, могат да бъдат променяни след първоначалното им задаване, но не допускат повторения!<br> Речниците имат ключове и стойности отговарящи на тези ключове.

## Синтаксис:
```py
myDict = {'name': 'Dani', 'age': 21, 'student': True}
print(myDict)
```
Ключовете в този речник са 'name', 'age', 'student'.<br>
Както виждате, стойностите могат да бъдат от всеки тип.<br>
Това важи и за ключовете.<br>
```py
myDict2 = {1: 'Dani'}
print(myDict2)
```


### По-подреден начин за писане на речници
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
```


## брой ключове/стойности
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
print(len(student))
```

## достъп до някоя стойност чрез ключа й
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
print(student['age'])
```

## промяна на стойност чрез ключа й
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
student['age'] = 40
print(student) # 40
```
#### Важно: не можем да променяме никой от ключовете, можем само да го премахнем!



## добавяне на нова двойка ключ-стойност към речника
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
student['from'] = 'Sofia'  
print(student)
```
Създава се ключ 'from' в речника, на който съотвества стойността 'Sofia'.<br><br>
Проблем при използването на [] е, че ако ключът не съществува, програмата ще ни хвърли изключние и програмата ще крашне.<br>
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
print(student['phone'])   # не съществува такъв ключ и програмата ще хвърли грешка.
```
### затова използваме get() функцията
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
print(student.get('age')) 
print(student.get('phone')) # принтира None, тъй като не съществува такъв ключ
print(student.get('phone', "Not found!"))  # променяме стойността, която връщаме ако не съществува такъв ключ
```

## Принтиране на различни елементи на речника:
### принтиране само на ключовете в речника:
```py
print(student.keys())
```

### принтиране само на стойностите в речника
```py
print(student.values())
```

### извличане на ключовете и стойностите като наредени двойки
```py
print(student.items())
```


## Важно
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
x = student.keys()
y = student.values()
z = student.items()
student['phone'] = '123'  # ключът 'phone' ще се добави към   х,    стойността '123' ще се добави към   у
print(x) 
print(y)
print(z)
```



## проверка дали някой ключ се намира в речника
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
if "phone" in student:
    print("yes")
```



## промяна на елементи в речника
### Вариант 1
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
student["name"] = "Georgi"
print(student)
```

### вариант 2: използвайки update()
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
student.update({"name": "Spas"})
```

### можем да променяме и няколко стойности наведнъж с update()
```py
student.update({"name": "Daniel", "age": 21})
print(student)
```

### използвайки update() можем и да добавяме нови двойки ключ-стойност
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"]
}
student.update({"phone": "123123", "addres": "Sofia"})
print(student)
```



## Премахване на елементи от речник 
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"],
    "phone": "123123"
}
```

### Вариант 1: 
pop() -> премахва item по зададен ключ от нас
```py
student.pop("phone")  
print(student)
```
Тук кодът премахва двойката (ключ-стойност), на която съотества ключа "phone"

### Вариант 2: 
popitem() -> премахва последния item  (ключ-стойност) 
```py
student.popitem()
print(student)
```


### Вариант 3:
Използвайки del()
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"],
    "phone": "123123"
}
del student["phone"]
print(student)
```
Не препоръчваме този начин, тъй като борави в паметта на компютъра и можем да изтрием данни, до които всъщност нямаме достъп, което значи, че програмата ни ще хвърли изключение.<br><br>
### Вариант 4:
Използвайки clear() можем да си изпразним речника.
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"],
    "phone": "123123"
}
student.clear()
print(student)
```



## Итериране в речник

```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"],
    "phone": "123123"
}
```

## принтиране на ключовете
### начин 1:
```py
for x in student:
    print(x)
```

### начин 2:
```py
for x in student.keys():
    print(x)
```



## принтиране на стойностите
### начин 1:
```py
for x in student.values():
    print(x)
```

### начин 2:
```py
for x in student:
    print(student[x])
```

## ВАЖНО!
### Принтиране на ключ и стойност!
```py
for x,y in student.items():
    print(x, y)
```
Тук x съответства на ключа, а у на стойността. Независимо как именуваме променливите,
първата винаги съответства на ключа, а втората на стойността!<br>


## копиране на речници:
```py
student = {
    "name": "Ivan",
    "age": 25,
    "courses": ["Algebra", "DIS", "Introduction to Programming"],
    "phone": "123123"
}
```

### начин 1:
```py
student2 = student.copy()
print(student2)
```

### начин 2:
```py
student3 = dict(student)
print(student3)
```



## Nested речници

### начин 1:
```py
child1 = {"name": "Dani", 'age': 20}
child2 = {"name": "Pesho", "age": 15}
children = {
    "child1": child1,
    "child2": child2
}
print(children)
```

### начин 2:
```py
myfamily = {
  "child1" : {
    "name" : "Emil",
    "age" : 25
  },
  "child2" : {
    "name" : "Georgi",
    "age" : 24
  },
  "child3" : {
    "name" : "Ivan",
    "age" : 27
  }
}
print(myfamily)
```


## Методи за речници:
- clear()	Removes all the elements from the dictionary
- copy()	Returns a copy of the dictionary
- fromkeys()	Returns a dictionary with the specified keys and value
- get()	Returns the value of the specified key
- items()	Returns a list containing a tuple for each key value pair
- keys()	Returns a list containing the dictionary's keys
- pop()	Removes the element with the specified key
- popitem()	Removes the last inserted key-value pair
- setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
- update()	Updates the dictionary with the specified key-value pairs
- values()	Returns a list of all the values in the dictionary