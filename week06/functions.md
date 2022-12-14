# Функции
## дефиниция на функция:
### Функция е дефинирано парче код, което се изпълнява в програмата ни само когато го повикаме. <br>На една функция можем да подаваме данни(параметри) <br>и една функция може да връща резултат

## Синтаксис:
Дефинираме функция по следния начин:
```py
def myFunc(): 
    pass

print(myFunc())
```
def дефинира функцията myFunc, която няма параметри.<br>
В случая функцията не прави нищо.<br>
pass означава, че функцията не прави нищо. (пишем pass за да не ни гръмне програмата)<br>
Ако извикаме метода print() и в него функцията, на екрана ще се принтира None, тъй като функцията не прави нищо и не връща резултат.<br>
Ако искаме да принтира нещо различно от None, то функцията трябва да върне резултат.


## извикване на функция
```py
def myName():
    print("Dani")

myName() # извиква функцията myName, която на свой ред принтира "Dani"
```


## пример на това защо използваме функции:
Нека например от нас се иска да принтираме Hello World! 4 пъти. Ще го направим по следния начин:<br>
```py
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
```
Сега си представете, че шефът ни ни казва, че не харесва тази удивителна накрая на изречението и иска да я премахнем.<br> 
Как става това - като променим кода:
```py
print("Hello World.")
print("Hello World.")
print("Hello World.")
print("Hello World.")
```
Проблемът тук е, че променяме кода на 4 места, а ако използваме функция може да променим само 1:<br>
```py
def hi():
    print("Hello World!")

hi()
hi()
hi()
hi()
```
И сега ако от нас се иска да махнем "!", можем просто да променим един ред, а не 4<br>
В случая 4 реда код не е много за промяна, но представете си че става дума за хиляди редове<br>
Eднакъв код, на който трябва да му се смени един символ, и отгоре на това в различни файлове..<br>
Много по-лесно е да използваме функция<br>
Това всъщност се нарича да си държим кода сух (DRY -> Dont Repeat Yourself)<br>
 



## Аргументи във функции
```py
def sayHi(name):
    print(f"Hi, {name}!")

sayHi("Dani") # подаваме аргумент "Dani" на функцията като я извикваме
sayHi(2)
```
В този пример функцията sayHi приема аргумент name и го използва в себе си (не е задължително да го ползва, но няма логика да не го)

## разлика между параметър и аргумент:
<b>Параметрите</b> са променливите, които обозначаваме че очакваме да бъдат подадени в нашата функция<br>
<b>Aргументите</b> са променливите, които подавме на функцията при извикването й<br>
<br>
Tрябва да подаваме точния брой аргументи на функцията, иначе ще получим компилационна грешка!<br>

```py
def myFunc(fname, lname):
    print(f"{fname} {lname}")
myFunc("Daniel", "Ivanov")
```
В този случай функцията ще работи.
```py
def myFunc(fname, lname):
    print(f"{fname} {lname}")
myFunc("Daniel")
myFunc("Daniel", "Stoqn", "Mihail")
```
А в този случай ще получим компилационна грешка.

### *args
Aко не знаем броя на аргументите, които очакваме, можем да напишем *args като параметър на функцията:
```py
def hiAll(*names):
    print(f"Hello, {names[0]}, {names[1]}!")

hiAll("Daniel", "Stoqn", "Kiril")
```
Разбира се, трябва да внимаваме да не поискаме 5тия аргумент като сме получили 3, защото ще получим error.



## keyword аргументи
```py
def hiAll(name3, name2, name1):
    print(f"Hi {name1}, {name2}, {name3}")

hiAll(name1 = "Dani", name2 = "Kiril", name3 = "Stoyan") # по този начин пренареждаме имената както ние искаме да ги подадем
```
Горе във функцията параметрите започват от 3 към 1, а долу като аргументи подаваме от 1 към 3!<br>
Това е възможно само чрез подаване на аргументите като keywords.




## Какво правим при незнаен брой keyword аргументи
По стандарт се пишат **kwargs
```py
def sayHi(**kid): # очакваме keyword аргументи, но не знаем нито какви, нито колко
    print("Hello" + " " + kid["fname"] + " " + kid["lname"])

sayHi(fname = "Daniel", lname = "Ivanov") # подаваме keyword аргументите си
```


## Default-на стойност на параметър
```py
def myName(name = "Dani"):
    print(name)

myName() # викаме функцията без да подаваме аргумент и слага default-ната стойност Dani като аргумент към параметъра
myName("Stoyan") # викаме функцията и подаваме аргумент "Stoyan", който презаписва default-ната стойност
```


 
## *args и **kwargs заедно в една функция
```py
def myFunc(*args, **kwargs):
    for x in args:
        print(x)
    for x in kwargs:
        print(x)

myFunc("Dani", "Misho", "Stoyan", dani = "Dani1", misho="Misho1", stoyan="Stoyan1")
```
- Dani, Misho, Stoyan са в args, тъй като нямат keyword
- Dani1, Misho1, Stoyan1 са в kwargs, тъй като имат keyword
<br>
Mожете да променяте args и kwargs на каквото поискате, важни са *-те отпред, те обозначават.




## подаване на структура от данни като аргумент:
```py
list = ["apple", "cherry", "banana"]
def printFruits(food):
    for x in food:
        print(x)

printFruits(list)
```





## Return стойност на функция
Kакто казахме, функциите могат и да връщат стойности, сега ще покажем как точно.
Чрез запазената дума return обозначаваме какво ще върне нашата функция
```py
def myFunc():
    return 1

myFunc() # няма да се случи нищо, защото функцията просто връща числото 1 
print(myFunc()) # ще принтира 1, а 1 идва като return стойност от функцията


def timesFive(x):
    return x*5

print(timesFive(15)) # 75
```