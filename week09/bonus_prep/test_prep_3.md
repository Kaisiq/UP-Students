# Решение – подготовка за контролно, задача 3

Функцията връща речник с броя срещания на всеки символ.

```py
def countSymbols(text):
    symbols = {}
    for ch in text:
        if ch in symbols:
            symbols[ch] += 1
        else:
            symbols[ch] = 1
    return symbols


print(countSymbols("obicham da karam kolelo"))
```
