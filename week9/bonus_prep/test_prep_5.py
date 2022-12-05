
def gcd(number1, number2):
    Min = min(number1, number2)
    Max = max(number1, number2)
    if Min == 0:
        return Max
    return gcd(Min, Max%Min)
    
print(gcd(18,84))