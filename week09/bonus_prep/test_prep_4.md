# Решение – подготовка за контролно, задача 4

Функцията обхожда вложен списък рекурсивно и сумира числата в него.

```py
def sumlist(lst):
    total = 0
    for item in lst:
        if type(item) is list:
            total += sumlist(item)
        else:
            total += item
    return total


print(sumlist([1, 2, [3, 4], [[5], 6]]))
```
