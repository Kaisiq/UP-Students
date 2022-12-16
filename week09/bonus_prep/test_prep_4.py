# [ 1 , 2 , [3 , 4] , [[5], 6] ] -> 21

# [3 , 4] -> 7

# [[5], 6] -> sum = 5 + 6 = 11

# [ 5 ] -> 5


def sumlist(lst):
    length = len(lst)
    sum = 0
    for i in range(0,length):
        if type(lst[i]) is type([]):
            sum = sum + sumlist(lst[i])
        else:
            sum += lst[i]
    return sum

print(sumlist( [1,2,[3,4],[[5],6]] ) )