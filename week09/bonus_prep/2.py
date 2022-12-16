def generateAn(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    elif n == 1:
        return 2

    elif n == 2:
        return 4

    elif n == 3:
        return 8

    else:
        return generateAn(n-1) * generateAn(n-3) - generateAn(n-2) * generateAn(n-4)




def generateFirstN(n):

    lst = []
    for i in range(0, n):
        lst.append(generateAn(i))
    return lst



# print( generateFirstN(100000) )




# 1в)

#2, 3, 6, 18, 108... (Cn = Cn-1 * Cn-2)

def generateListUntilN(n):
    lst = [2, 3]
    for i in range(2, n+1):
        Ci = lst[i-1] * lst[i-2]
        lst.append(Ci)
    return lst

print(generateListUntilN(7))



def generateCn(n):
    if n < 0:
        return 1
    if n == 0:
        return 2
    elif n == 1:
        return 3
    else:
        return generateCn(n-1) * generateCn(n-2)

def genUntilN(n):
    lst = []
    for i in range(0,n):
        lst.append(generateCn(i))
    return lst


