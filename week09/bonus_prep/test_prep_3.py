def countSymbols(str):
    symbols = {}
    for ch in str:
        if ch in symbols:
            n = symbols[ch]
            symbols[ch] = n + 1
        else:
            symbols[ch] = 1

    return symbols

print(countSymbols("obicham da karam kolelo"))