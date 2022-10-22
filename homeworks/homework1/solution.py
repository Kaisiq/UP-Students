# Задача 1

a = int(input("enter a: "))
b = int(input("enter b: "))
c = (a**2+b**2)**(1/2)
p = (a+b+c)/2
s = a*b/2
hc = (a*b)/c
mc = c/2
lc = (a*b)/(a+b) * (2**(1/2))

print('б) лице: ',s)
print('в) хипотенуза : ',c)
print('г) височина: ', hc,
    '\n   медиана: ', mc,
    '\n   ъглополовяща: ', lc)

# забележете, че когато искам да коренувам, вместо да ползвам math,
# степенувам на степен 1/2, което точно ми върши работата.




# Задача 2
str = input("enter string: ")


#б) забележете. че броим започвайки от 0!
strB = ""
for index in range(len(str)):
    if index % 2 == 1 :
        strB += str[index].upper()
    else:
        strB += str[index].lower()
print("б)", strB)

#в)
backS = str[::-1]
print("в)", backS)

#г)
print("г)", str == str[::-1])