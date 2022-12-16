# Редици  

### Редиците се използват за съхраняване на голям брой данни в една променлива.<br>Елементите в редиците са номерирани и за разлика от листите, елементите на редиците не могат да бъдат променяни след първоначалното им задаване.<br>Tова означава, че също така не можем да добавяме и премахваме елементи към редиците.

## Синтаксис:
```python
mytuple = ("apple", "banana", "cherry")
print(mytuple)
```

### За да направим редица само с един елемент, задължително трябва да има запетайка след него
```python
oneElementTuple = ("apple",)
print(type(oneElementTuple))
```

това например не е редица:
```python
notTuple = ("apple")
print(type(notTuple)) # string
```


### Редиците, като листите, могат да съдържат елементи от различен тип
```python
tuple1 = ("abv", 12, True, 42, "hello")
```

## Дължина на редица
```python
print(len(mytuple))
```

## Достъп до елемент на редица
Kакто при string и list
```python
mytuple = ("abv", 12, True, 42, "hello", False)
print(mytuple[1]) # 12
```


### Обратно индексиране
```python
print(mytuple[-1])
```
### Принтиране на избрани елементи по индекси
```python
print(mytuple[1:3])
```

## Проверка дали някой елемент принадлежи на редица
```python
mytuple = ("abv", 12, True, 42, "hello", False)
if 12 in mytuple:
    print("yes")
if 24 in mytuple:
    print("yes2")
```



## Промяна на елемент в редица
Tъй като редиците са immutable, техните елементи не могат да бъдат променяни.<br>
Но ако много искаме да променим някой елемент, можем да направим лист от редицата,<br>
да променим елемента и след това да направим редица от този лист.<br><br>
За тази цел ще използваме list() и tuple(), които създават лист/редица от подадените елементи на функцията.
### Пример:
```python
tuple1 = ("apple", "banana", "cherry")
list1 = list(tuple1) # взима елементите на tuple1 и създава лист от тях
print(list1)
list1[1] = "mango"
print(list1) # след промяната
tuple1 = tuple(list1) # взима елементите на list1, създава редица от тях и я присвоява на tuple1
print(tuple1)
```
Чрез тази техника можем да добавяме и премахваме елементи към редиците,<br>
като за целта създаваме лист от елементите на редицата,<br>
извършваме всички операции които искаме<br>
и след това създаваме редица от елементите на новополученият лист.<br>



### Друг подход:
Забележете, че работи само за добавяне, а не за премахване и промяна!
```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("mango",)
tuple2 += tuple1
print(tuple2)
```
Tова парче код реално работи по следния начин:<br>
- двете редици се променят към листи;
- двата листа се смесват в един;
- резултатът се променя обратно към редица, която се присвоява на tuple2

### Бонус:
Събиране на една редица със себе си няколко пъти
```python
tuple1 = ("apple", "banana", "cherry")
tuple1 += tuple1
print(tuple1)
tuple2 = ("apple", "banana", "cherry")
tuple2 = tuple2 * 5
print(tuple2)
```
<br><br>
### премахването на елемент от редица става само чрез използване на листи!




## Разопаковане на редица 
```py
plodove = ("apple", "banana", "mango")
(a, b, c) = plodove 
# a = "apple"
# b = "banana"
# c = "mango"
print(a)
print(b)
print(c)



plodove = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a, b, *c) = plodove
print(a)
print(b)
print(c) # ['cherry', 'strawberry', 'raspberry']



plodove = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a, *b, c) = plodove
print(a)
print(b) # ['banana', 'cherry', 'strawberry']
print(c) # "raspberry"
```



## Итериране в редица
Aбсолютно същото както при листите
```py
tuple = ("apple", "bed", "wall", "banana", "mango")
for x in tuple: 
    print(x) 



for x in range(len(tuple)):
    print(tuple[x])



i = 0
while(i < len(tuple)):
    print(tuple[i])
    i+=1
```


Други методи с редици:<br>
count()	Returns the number of times a specified value occurs in a tuple<br>
index()	Searches the tuple for a specified value and returns the position of where it was found<br>