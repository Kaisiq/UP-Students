# Булеви стойности и условни оператори

## Тип `bool` и оператори за сравнение

```py
print(True)
print(False)
print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(69))
print(bool(False))
print(bool(None))
print(bool(0))
```

Празните низове, `0`, `None` и празните структури от данни имат булева стойност `False`; повечето други стойности имат `True`.

```py
x = 5
y = 12
print(x == y)  # Equal
print(x != y)  # Not equal
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

x = 1
y = 2
z = 3
print(x < y and y < z)
print(x < y or y > z)
print(not (x > y or y < z))

print(x is y)
print(x is not y)

s = "Obicham da ucha vuv fmi!"
print("fmi" in s)
print("fmi" not in s)
```

## Побитови операции

```text
&   побитово И
|   побитово ИЛИ
^   побитово изключващо ИЛИ
~   побитово отрицание
<<  изместване на битовете наляво
>>  изместване на битовете надясно
```

Например двоичното представяне на `1`, `2`, `3` и `15` е съответно `1`, `10`, `11` и `1111`.

## `if`, `elif` и `else`

Отстъпът определя тялото на условния блок. Неправилен синтаксис или отстъп води до синтактични грешки.

```py
if <проверка>:
    <код>
<друг код>
```

```py
a = 15
b = 25
if a > b:
    print("Mrazim FMI")
print("shegichka")

if a < b:
    print("Obichame FMI")

a = 15
b = 15
if a > b:
    print("111")
else:
    print("222")
```

```py
a = 15
b = 15
if a > b:
    print(1)
elif a < b:
    print(2)
elif a == b:  # използваме ==, а не =
    print(3)

if a > b:
    print("a is greater than b")

print(a) if a > b else print(b)
```

## Вложени условия

```py
a = 5
b = 10
c = 7
if a < b and a < c and c < b:
    print("a < c < b")

a = 20
if a > 10:
    print("a e по-голямо от 10")
    if a > 20:
        print("a e по-голямо от 20")
    else:
        print("но не е по-голямо от 20")
else:
    print("a не е по-голямо от 10")
```

## Упражнение

Напишете програма, която приема трите страни `A`, `B` и `C` на триъгълник и проверява дали образуват истински триъгълник: `A + B > C`, `A + C > B` и `B + C > A`.
