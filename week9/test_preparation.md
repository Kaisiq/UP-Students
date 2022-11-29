# Подготовка за контролно №2

### Решенията на всяка задача да бъдат под формата на функции!

## Задача 1
Генерирайте първите N члена (в редици) на следните редици:
- 1, 3, 6, 9, 12... (An = n*3)
- 1, 1, 2, 3, 5... (Bn = Bn-1 + Bn-2)
- 2, 3, 6, 18, 108... (Cn = Cn-1 * Cn-2)
Слейте трите резултатни редици в една, като събирате елементите на съответните позиции.

## Задача 2
Напишете функция, която получава като параметър символен низ (телефонен номер) и проверява дали е валиден български телефонен номер:
- започва с +
- всички останали символи освен първия са числа
- дължината на номера е точно 13 символа
- българските номера започват с +359



## Задача 3
Напишете функция, която приема като параметър символен низ. Да се изведе колко пъти се среща всеки символ в низа. Ако някой символ се среща повече от веднъж, да не се принтира повторно колко пъти се среща.<br>
Вход: "obicham da karam kolelo"
Изход: 
```
o -> 3
b -> 1
i -> 1
c -> 1
h -> 1
a -> 4
m -> 2
' '(space) -> 3
d -> 1
k -> 2
r -> 1
l -> 2
e -> 1
```




## Задача 4
Напишете функция, която сумира елементите на вложен списък.<br>
Пример:<br>
Вход: [1,2,[3,4],[[5],6]]<br>
Изход: 21

## Задача 5
Напишете функция, която намира най-големия общ делител на две цели числа.



<br><br><br><br><br><br>

## Допълнителна задача

A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.<br>
Example:
```
n = 4
m = 6
s = 2
```


There are 4 prisoners, 6 pieces of candy and distribution starts at chair 2. The prisoners arrange themselves in seats numbered 1 to 4. Prisoners receive candy at positions 2,3,4,1,2,3. The prisoner to be warned sits in chair number 3.