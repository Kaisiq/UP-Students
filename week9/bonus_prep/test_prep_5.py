def nod(number1, number2):
    n = 0
    minimal = min(number1, number2)
    for i in range(2, minimal):
        if number1 % i == 0 and number2 % i == 0:
            n = i

    return n

print(nod(18, 84))



def gcd(number1, number2):
    Min = min(number1, number2)
    Max = max(number1, number2)
    if Min == 0:
        return Max
    return gcd(Min, Max%Min)
    
print(gcd(18,84))