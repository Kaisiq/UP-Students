# Решение – подготовка за контролно, задача 5

Първият пример използва обхождане, а вторият е рекурсивният алгоритъм на Евклид.

```py
def nod(number1, number2):
    result = 0
    minimal = min(number1, number2)
    for i in range(2, minimal):
        if number1 % i == 0 and number2 % i == 0:
            result = i
    return result


print(nod(18, 84))


def gcd(number1, number2):
    minimum = min(number1, number2)
    maximum = max(number1, number2)
    if minimum == 0:
        return maximum
    return gcd(minimum, maximum % minimum)


print(gcd(18, 84))
```
