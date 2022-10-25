# Лист

### Листите са колекция от елементи и се използват за съхраняване на голям брой данни в една променлива.<br> Те са един от 4те вградени типове в Python, заедно с <b>речниците</b>, <b>редиците</b> и <b>множествата</b>. <br>Данните в листите могат да бъдат променяни след първоначалното им задаване.


## Синтаксис:
Инициализираме променливата като й задаваме име и след това в прави скоби "[]" изреждаме елементите, които ще съдържа
```python
mylist = ["apple", "banana", "cherry", "mango"]
```



В един лист може да съхраняваме различни типове данни, както примитивни, така и съставни.
```python
mylist = ["apple", 15, True, "banana"]
mylist2 = [["apple", 15, True], False, "banana", -23.43]
```

Елементите на списъка са индексирани, започващи от 0<br>
Достъпването на елемент от списъка работи по същия начин както и при string-овете (чрез оператор []).
```python
mylist = ["apple", 15, True, "banana"]
print(mylist[0]) # ще принтира "apple" на екрана
```



Разбира се, тук също има обратно индексиране:
```python
mylist = ["apple", 15, True, "banana"]
print(mylist[-1]) # "banana"
```


Можем и да принтираме избран отрязък от листа.
```python
mylist = ["apple", 15, True, "banana"]
print(mylist[1:3]) # [15, True]
```




Елементите на лист могат да бъдат променяни след като веднъж са били зададени:
```python
mylist = ["apple", 15, True, "banana"]
mylist[0] = "not apple"
print(mylist[0])
```
Тук достъпваме елемента на позиция 0 ("apple") и му присвояваме новата стойност "not apple"<br><br>


Също, тъй като всички елементи са индексирани, може да има повторения на елементи:
```python
mylist = ["a", "a", "b", "a", "b"]
print(mylist)
```

### дължина на списък 
Дължината на един list се намира точно както при string-овете, използвайки вградения метод len().
```python
mylist = ["a", "a", "b", "a", "b"]
print(len(mylist)) # точно както при string-овете
```

### Тип на списък
Можем да проверим какъв тип е всяка променлива, включително списъците, с метода type().
```python
mylist = ["a", "a", "b", "a", "b"]
print(type(mylist)) # типът на листите е class 'list'
```

## Добавяне на нов елемент
### Добавяне на позиция, избрана от нас
```python
mylist = ["1", "2", "3", "4" ,"5" ,"7"]
mylist.insert(5, "6") # insert-ва "6" на позиция 5 в масива
print(mylist)
```
Не забравяйте, че винаги започваме да броим елементите от 0!

### добавяне в края
Добавянето на елемент в края на лист се случва чрез използването на вградения метод за листи append().
```python
mylist = ["1", "2", "3", "4" ,"5" ,"7"]
mylist.append("8")
print(mylist)
```


## Премахване на елемент от списък
### премахване на специфичен елемент
Премахването на специфичен елемент зададен от нас се случва с метода remove().<br>
Той премахва първият срещнат елемент със стойност аргумента който сме подали на remove().
```python
mylist = ["apple", "banana", "mango"]
mylist.remove("banana") # премахва първия срещнат елемент със стойност "banana"
print(mylist)

mylist = ["apple", "banana", "mango", "banana"]
mylist.remove("banana")
print(mylist)
```


### премахване на елемент по подаден индекс
Премахването на елемент по подаден индекс се случва използвайки метода pop(), на който подаваме индекса на елемента, който искаме да премахнем.<br>
Не забравяйте, че броим от 0!<br>
Ако не подадем аргумент на метода pop(), то той премахва последния елемент от листа.
```python
mylist = ["apple", "banana", "mango", "banana"]
mylist.pop(2) # премахва "mango"
print(mylist)
mylist.pop()  # премахва елемента на последната позиция ("banana")
print(mylist)
```

### изпразване на целия списък
Случва се чрез метода clear()
```python
mylist = ["apple", "banana", "mango", "banana"]
mylist.clear()
print(mylist) # []
```

##  Итериране в лист 
възможно е както с for, така и с while, но е много по-лесно с for
### Пример с for
```python
mylist = ["apple", "bed", "wall", "banana", "mango"]
for x in mylist:
    print(x) 
```
Тук хващаме всеки елемент от mylist един по един на всяко завъртане от цикъла.


### Пример с in range
```python
for x in range(len(mylist)):
    print(mylist[x]) 
```
В този цикъл x варира от 0 до дължината на mylist и принтираме елемента на позиция x в mylist.

### пример с while цикъл
Същият пример, но използвайки while цикъл.<br>
Не забравяйте, че while циклите винаги трябва да имат стъпка.
```python
i = 0
while(i < len(mylist)):
    print(mylist[i])
    i+=1
```


## Разбиване на лист

### начин 1
```python
plodove = ["apple", "banana", "mango", "grapefruit", "kiwi"]
new_plodove = []
for x in plodove:
    if "n" in x:
        new_plodove.append(x)

print(new_plodove)
```


### начин 2 - интуитивен, но грозен код (не го препоръчваме)
```python
plodove = ["apple", "banana", "mango", "grapefruit", "kiwi"]
new_plodove = [x for x in plodove if "n" in x]  
print(new_plodove)
```


## сортиране на лист
```python
plodove = ["apple", "banana", "mango", "grapefruit", "kiwi"]
plodove.sort() # сортира по азбучен ред   // сортирането е case sensitive!!!    
print(plodove)



chisla = [5, 16, 3, 7, 1240, 3, 1, 2]
chisla.sort() # сортира от най-малко към най-голямо число
print(chisla)
```

### обратно сортиране
```python
chisla = [5, 16, 3, 7, 1240, 3, 1, 2]
chisla.sort(reverse= True)
print(chisla)
```


## копиране на лист 
### вариант 1
използвайки метода copy()
```python
chisla = [5, 16, 3, 7, 1240, 3, 1, 2]
list2 = chisla.copy()
print(list2)
```

### вариант 2 
използвайки конструктора на list (не го препоръчваме засега, защото няма да разберете как точно работи)
```python
chisla = [5, 16, 3, 7, 1240, 3, 1, 2]
list2 = list(chisla)
print(list2)
```


## конкатенация на листи 
### вариант 1 - най-лесен, като при стринговете
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2  # подобно на string-овете
print(list3)
```
Разбира се, тук можем да използваме и +=


### вариант 2 - използвайки append()
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
```

#### вариант 3 - използвайки вградената функция extend()
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
```



### Всички методи с листи:
- append()	Adds an element at the end of the list
- clear()	Removes all the elements from the list
- copy()	Returns a copy of the list
- count()	Returns the number of elements with the specified value
- extend()	Add the elements of a list (or any iterable), to the end of the current list
- index()	Returns the index of the first element with the specified value
- insert()	Adds an element at the specified position
- pop()	Removes the element at the specified position
- remove()	Removes the item with the specified value
- reverse()	Reverses the order of the list
- sort()	Sorts the list