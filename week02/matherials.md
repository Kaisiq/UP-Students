# Материали върху числа и символни низове

## Cast-ване на типове към други 
### от предния път
```py
x = int(1)
y = int(2.8)
z = int("3")
```
x ще се кастне към 1
y ще се кастне към 2
z ще се кастне към 3
<br>

### ново
```py
x = float(1)     # x ще стане 1.0
y = float(2.8)   # y ще стане 2.8
z = float("3")   # z ще стане 3.0
w = float("4.2") # w ще стане 4.2

x = str("s1") # x ще стане 's1'
y = str(2)    # y ще стане '2'
z = str(3.0)  # z ще стане '3.0'
```

### Важно!
Променливите в python, както и във всеки друг език за програмиране са <b>Case Sensitive</b>!
```py
d = "Hello World"
print(d)
```
Това парче код ще ни принтира Hello World на екрана.
<br>
<br>

```py
d = "Hello World"
print(D)   #<- case sensitive
```
Това парче код обаче би било крашнало ако се опитаме да го run-нем. Това е защото променливата "D" не съществува в нашата програма, а ние се опитваме да я принтираме.



# Символни низове / String

Няма значение какви кавички ползваме в print() ф-ята.   Независимо дали " или ' резултатът е един и същ
```py
print("Hello")
print('Hello')
```



## Символен низ на няколко реда

```py
s = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(s)
```


## Конкатенация на символни низове
"+" конкатенира string-ове, като не добавя разстояние между тях. Забележете как изкуствено си добавяме разстояние след Hello.
```py
x = "Hello "
y = "world!"
print(x + y) # "Hello world!"
```

### Съвет
Добавяйте си space-а на ръка в print функцията, за да ви е по-нагледно
```py
x = "Hello"
y = "world!"
print(x + " " + y)
```
<br>

Разбира се, не е нужно да пишем x + y в print() функцията, можем да си направим нова променлива която да е равна на x+y
```py
x = "Hello"
y = "world!"
z = x + " " + y
print(z)
```
<br><br>

","  конкатенира string-ове като добавя разстояние между тях
```py
x = "Hello"
y = "World"
print(x,y)
```

### Важно!
Не можем да принтираме число и символен низ, като ги конкатенираме с "+", тъй като плюсът индикира, че искаме да съберем числото със символният низ и компилаторът се обърква и ни крашва програмата.
```py
x = 5
y = "String"
print(x + y) #няма да проработи, защото  +  опитва да събере числото със string-a
print(x , y) # 5 String
```

<br><br>

```py
y = "3"
print(x + y)
```
print(x + y) няма автоматично да смени типа на Y на int и да ги събере, тоест ще има грешка


## Представяне на string като редица от символи
Hello
|H|e|l|l|o|

```py
s = "Hello"
```
С квадратни скобки "[]" можем да достъпим избран символ от редицата от символи<br>

### ВАЖНО - броенето винаги започва от 0, а НЕ от 1

```py
print(s[0]) # H
print(s[1] + s[3]) # ?
```


## Дължина на дума
```py
s = "Hello World!"
daljina = len(s)
print(daljina) # 12
```

## Проверка дали substring се съдържа в string
```py
s = "Obicham da ucha vuv fmi!"
print("fmi" in s)   #  А какъв е типът на това което ще принтираме?
```

## Проверка дали substring не се съдържа в string
```py
s = "Obicham da ucha vuv fmi!"
print("fmi" not in s)
```



## Одрязване на string
```py
s = "Hello World!"
print(s[2:5])
```
отново ползваме [] за да достъпим символи с номерация от 2 до 4 (включително, без символът на място 5) в s
```py
print(s[:5]) # от нулевият сумвол до четвъртият включително
print(s[2:]) # от вторият символ до края
print(s[-5:-2])
```
Обратна индексация -> "-5" означава 5тият символ отзад напред



## Промяна на символен низ
### uppercase и lowercase

```py
s = "Hello world!"
print(s.upper()) # HELLO WORLD!
print(s.lower()) # hello world!
```

### премахване на табулации и разстояния отпред и отзад

```py
s = "      Hello world!            "
print(s) # принтира се с табулациите отпред и отзад
print(s.strip()) # принтира без разстояния отпред и отзад на текста
```


## замяна на един символ с друг в string
```py
s = "hello world"
print(s.replace('l', 'e'))
```


## split-ване на string
```py
s = "Hello world!"
print(s.split(" "))  # ['Hello', 'world!']
print(s.split("l"))  # ['He', '', 'o wor', 'd!']
```

## добавяне на кавички в string
```py
s = "Liubimiqt mi serial e \"Alice in Borderland\"!"
```

```
\" -> "
\' -> '
\\ -> \
\n -> нов ред
\t -> табулация
```
Има и други, но това са основните които ще ползвате

## форматиране на символен низ
```py
name = "Vili"
age = 21
print(f"I am {name}, {age} years old.")
```
"f" форматира текста, използвайки горните променливи и ги замества

```py
print("I am" , name, ",", age, "years old.")
```
Работи подобно на горното, но имайте впредвид екстра whitespace-а, който се добавя заради ","


## Split-ване на символен низ
```py
txt = "hello, my name is Dani. I am 21 years old"
x = txt.split() #any whitespace
print(x)

txt = "hello, my name is Daniel, I am 21 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
```






## .join()
```py
myList = ["apple", "banana", "mango"]
txt = " ".join(myList)
print(txt)

txt = "DANI".join(myList)
print(txt)

separator = ".I love "
txt = separator.join(myList)
print(txt)
```


## Бонус информация: 
https://www.geeksforgeeks.org/python-string-methods/