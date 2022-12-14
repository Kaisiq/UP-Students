# Материали относно Цикли : for и while

### Има два типа цикли:
#### while цикли:
- Състоят се от проверка и се изпълняват докато тази проверка се удовлетворява(true)
#### for цикли:
- Използват се за итериране през някаква редица от елементи (масиви, редици, листи). Засега ще го ползваме за изпълняване на цикъля определен брой пъти.

# While цикъл

## пример за while цикъл
```py
i = 0
while(i < 5):
    print(i)
    i+=1     
```
### ВАЖНО
Aко редът, където инкрементираме i с 1 го нямаше, цикълът ще продължава безкрайно, защото проверката винаги ще е <b>true</b><br>
Изход:
```
0 
1 
2 
3 
4
```
Kакво трябва да променим в кода за да принтираме числата от 0 до 5 включително?

<br><br>
Въпрос:
Защо следният цикъл е безкраен?

```py
i = 5
while(i < 500):
    print(i)
    i-=1
```


## break statement в while цикъл
break прекъсва изпълнението на цикъла и директно излизаме от тялото му, продължавайки с кода надолу
```py
i = 0
while(i < 15):
    print(i)
    if(i == 10):
        break
    i+=1
```




## continue statement в while цикъл
continue казва на цикъла да пропусне всички редове надолу в тялото на цикъла и директно да отиде горе и да продължи със завъртането на цикъла.
```py
i = 0
while(i < 15):
    i+=1
    if(i % 2 == 0):
        continue
    print(i)
```
Ако инкрементацията на i беше под continue, цикълът щеше да е безкраен, тъй като няма да инкрементираме i и всеки път ще влизаме в if-а.



# For цикъл
## пример за for цикъл
```py
for i in range(6):
    print(i)
```
Изход:
```
0 
1 
2 
3 
4 
5
```

### range() е функция приемаща 3 аргумента:
- стартово число, крайно число, стъпка - точно като [] при string-ове<br>
- стартовото число по default е 0
- крайното число винаги трябва да бъде зададено от нас, няма default-на стойност
- стъпката по default е 1, тоест на всяко достигане на проверката в цикъла, стойността на i се увеличава с 1-ца

## пример за range() със зададени стойности от нас
```py
for i in range(15,250,3):
    print(i)
```
Това ще принтира 15, 18, .... , 249  -  всички кратни на 3 числа между 15 и 250, изключвайки 250

<br><br>

### нека преведем горния for цикъл във while цикъл: 
```py
i = 15
while(i < 250):
    print(i)
    i+=3
```
Можем да запишем всеки for цикъл като while, но е много по-удобно да ползваме for, тъй като при while циклите можем да забравим инкрементацията на i и да си крашнем програмата без да искаме


## при for цилките също можем да ползваме break и continue
```py
for i in range(500):
    if(i % 5 != 0): # i не се дели на 5 без остатък
        continue
    print(i)
```

```py
for i in range(0, 500, 129):
    if(i == 258):
        break
    print(i)
```

## бърза задачка:
Напишете цикъл, който принтира числата от 0 до 1000, които се делят на 13.<br>
След това напишете същият този цикъл използвайки стъпка, вместо if в тялото на цикъла.
