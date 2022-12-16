# map, filter, reduce, zip & unzip
Тази седмица ще разгледаме няколко вградени функции, които ще срещаме често в практиката и ще ни помагат при работата с данни.
## Map, Filter и Reduce
Това са 3 функции, които улесняват функционалния подход към програмирането. Ще разгледаме всеки един от тях и ще разберем защо, как и в какви случаи се използват.

### Map
map() прилага едноместна функция над всички елементи в лист, който подаваме като аргумент на метода map().
#### Синтаксис
```py
map(function_to_apply, list_of_inputs)
```
В почти всички случаи искаме да подадем елементите на лист-а към функцията един по един и след това да слепим изходите отново в лист, например:

```py
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

<br>
map() методът ни помага да имплементираме този код по по-лесен и кратък начин:

```py
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

В повечето случаи, в които използваме map(), функцията която подаваме като аргумент е всъщност ламбда функция.
<br><br>
Също така, освен да подаваме лист от елементи, можем да подадем дори и лист от функции!

```py
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
```

### Filter
Още като прочетем името на метода можем да заключим, че той филтрира елементи от лист и ги записва в резултат, който получаваме от метода.<br>
Методът получава едноместна <b>БУЛЕВА</b> функция и лист, който да филтрира, като връща само елементите, които са върнали резултат True при прилагането на функцията над тях.<br>
Пример: 

```py
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]
```

Филтърът представлява for цикъл, но е вградена функция и затова работи малко по-бързо.

### Reduce
reduce е много полезен метод за прилагане на някакво изчисление над лист при което се връща резултат под формата на един елемент(най-често число).<br>
Обикновеният начин, по който бихме решили такъв проблем е използвайки for цикъл:
```py
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24
```
<br>
Разбира се, можем да направим същото използвайки reduce() методът.<br>
Той приема двуместна функция и лист над който ще я приложи. Нека напишем същият код от горе, но използвайки reduce():

```py
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
```


## Zip и Unzip

### Zip
zip() е полезен метод, който ни позволява да обединяваме листове лесно.<br>
Пример:
```py
first_name = ['Joe','Earnst','Thomas','Martin','Charles']

last_name = ['Schmoe','Ehlmann','Fischer','Walter','Rogan','Green']

age = [23, 65, 11, 36, 83]

print(list(zip(first_name,last_name, age)))

# Output
#
# [('Joe', 'Schmoe', 23), ('Earnst', 'Ehlmann', 65), ('Thomas', 'Fischer', 11), ('Martin', 'Walter', 36), ('Charles', 'Rogan', 83)]
```

Плюсът на zip() е, че е много по-четим от еквивалента му с for цикли.<br>
Например, вместо да ни трябват няколко входни листа, се нуждаем само от един zip-нат лист от всички данни и да използваме един for цикъл:
```py
first_name = ['Joe','Earnst','Thomas','Martin','Charles']
last_name = ['Schmoe','Ehlmann','Fischer','Walter','Rogan','Green']
age = [23, 65, 11, 36, 83]

for first_name, last_name, age in zip(first_name, last_name, age):
    print(f"{first_name} {last_name} is {age} years old")

# Output
#
# Joe Schmoe is 23 years old
# Earnst Ehlmann is 65 years old
# Thomas Fischer is 11 years old
# Martin Walter is 36 years old
# Charles Rogan is 83 years old
```

### Unzip
Както за zip-ване, можем да използваме метода zip() и за unzip-ване на файлове. За целта обаче ще трябва да сложим "*" пред името на параметъра, за да обозначим, че очакваме вход от потребителя лист от елементи(в случая редици).<br>
Изходът е отделните елементи в лист-а, който сме подали като вход.
```py
full_name_list = [('Joe', 'Schmoe', 23),
                  ('Earnst', 'Ehlmann', 65),
                  ('Thomas', 'Fischer', 11),
                  ('Martin', 'Walter', 36),
                  ('Charles', 'Rogan', 83)]

first_name, last_name, age = list(zip(*full_name_list))
print(f"first name: {first_name}\nlast name: {last_name} \nage: {age}")

# Output

# first name: ('Joe', 'Earnst', 'Thomas', 'Martin', 'Charles')
# last name: ('Schmoe', 'Ehlmann', 'Fischer', 'Walter', 'Rogan')
# age: (23, 65, 11, 36, 83)
```