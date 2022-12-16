# Множества 
### Множествата се използват за съхраняване на голям брой данни в една променлива.<br>Елементите на множествата са неподредени, неиндексирани и не може да се променят.<br>Това значи, че може да се добавят нови елементи, могат и да се премахват елементи,<br>но един елемент не може да бъде променен, след като веднъж е добавен.<br>Това, че елементите са неиндексирани означава, че не може да има два елемента с еднаква стойност!<br>И последно, това че елементите са неподредени означава, че всеки път когато извикаме множеството, елементите могат да бъдат подредени по различен начин. 

## Синтаксис:
```py
myset = {"apple", "banana", "cherry"}
print(myset) # пуснете си програмата 2-3 пъти и вижте как поне веднъж ще са подредени различно
```


### Eдно множество може да съдържа различен тип променливи:
```py
set1 = {"abc", 34, True, 40, "male"}
```

## Дължина на множество
```py
print(len(myset))
```

## Достъп на елементи в множество
Няма как да ги достъпим по индекс, тъй като множествата са неиндексирани. <br>
Следователно можем само чрез for цикъл:
```py
myset = {"apple", "banana", "mango", "cherry"}
for x in myset:
    print(x)
```

## Проверка дали елемент се съдържа в множество
```py
myset = {"apple", "banana", "mango", "cherry"}
print("banana" in myset)

if "banana" in myset:
    print("yes")
```



## Добавяне на елементи към множество
```py
myset = {"apple", "banana", "mango", "cherry"}
myset.add("kiwi")
print(myset)
myset.add("banana") # няма да се добави втори път, тъй като не може да има повтарящи се елементи (неиндексиран, неподреден!)
print(myset)
```

## добавяне на set към set
### 1 начин:
Чрез метода update():
```py
set1 = {"apple", "banana", "mango"}
set2 = {"kiwi", "cherry"}
set1.update(set2)
print(set1)
```
### Втори начин:
Чрез метода union():
```py
set3 = set2.union(set1) # обедниява 2те множества и ги присвоява на set3
```

### Добавяне на list към set
```py
list1 = ["fmi", "matematika", 123]
set1.update(list1)
print(set1)
```



## Премахване на елемент от множество ===========>
Има няколко начина:

### начин 1:
```py
set = {"apple", "banana", "cherry"}
set.remove("banana")
```
проблемът на remove() е, че ако елементът който искаме да премахнем липсва, ще излезе грешка:
```py
set = {"apple", "banana", "cherry"}
set.remove("fmi") 
```


### начин 2:
```py
set = {"apple", "banana", "cherry"}
set.discard("banana")
set.discard("fmi")
```
discard() не хвърля грешка, ако елементът липсва.


### начин 3:
```py
set = {"apple", "banana", "cherry"}
set.pop()
```
pop() изхвърля последния елемент в структурата данни, но тук не знаем кой е последния, тоест премахваме <b>random</b> елемент.


### начин 4:
```py
set = {"apple", "banana", "cherry"}
set.clear()
print(set)
```
clear() изпразва множеството




## Други методи за множества

### пресичане на множества
```py
x = {"google", "fmi", "yahoo", "sofia"}
y = {"sofia", "varna", "burgas", "plovdiv"}
z = x.intersection(y)
x.intersection_update(y)
print(z)
print(x)
```


### симетрична разлика на множества
```py
x = {"google", "fmi", "yahoo", "sofia"}
y = {"sofia", "varna", "burgas", "plovdiv"}
z = x.symmetric_difference(y)
x.symmetric_difference_update(y)
print(z)
print(x)
```



## всички методи за set:
- add()	Adds an element to the set
- clear()	Removes all the elements from the set
- copy()	Returns a copy of the set
- difference()	Returns a set containing the difference between two or more sets
- difference_update()	Removes the items in this set that are also included in another, specified set
- discard()	Remove the specified item
- intersection()	Returns a set, that is the intersection of two other sets
- intersection_update()	Removes the items in this set that are not present in other, specified set(s)
- isdisjoint()	Returns whether two sets have a intersection or not
- issubset()	Returns whether another set contains this set or not
- issuperset()	Returns whether this set contains another set or not
- pop()	Removes an element from the set
- remove()	Removes the specified element
- symmetric_difference()	Returns a set with the symmetric differences of two sets
- symmetric_difference_update()	inserts the symmetric differences from this set and another
- union()	Return a set containing the union of sets
- update()	Update the set with the union of this set and others