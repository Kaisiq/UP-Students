# 4 задача
# [1,2,[3,4],[[5],6]] -> 21

def sumRec(ll):
    length = len(ll)
    sum = 0
    for i in range(length):
        if type(ll[i]) is type([]):
            sum += sumRec(ll[i])
        else:
            sum += ll[i]
    return sum

print(sumRec([1,2,[3,4],[[5],6]]) == 21) # check if example works


# 5 задача
def gcd(a,b):
    if b == 0:
        return abs(a)
    Min = min(a,b)
    Max = max(a,b)
    return gcd(Min, Max%Min)

print(gcd(60, 48)) #-> 12