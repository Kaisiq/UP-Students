print("Hello world!")
# Това е коментар



"""
Това е коментар
на няколко
реда!
"""








# Прости изчисления
35 + 15
15
"asd"





#Променливи
a = 15
b = 3
print(a)
print(b)

a = 16
print(a)








# Аритметични операции
a = 10
a+=1  #11
a = a + 1
a-=1  #10
b = a+1  #11
c = a-1  #9
d = a*2  #20
e = a/2  #5
f = a%3  #1
g = a//3 #3
h = a**2 #100

a = 10
a *= 2 # 10 * 2 = 20
a /= 2 # 20 / 2 = 10


c = a - b
print(c)
print(a-b)



x = 5
print(x)
x = 12
print(x)















#Именуване на променливи по правилния начин

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Именуване по грешния начин
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""










"""
Вградени типове данни:
    "Примитивни" типове:
        Цели числа / Integer  ->  3; 12; 15; 5000; 102405125
        Числа с плаваща запетая / Float  -> 12.3; 3.14; 512512.1241231
        Булеви / Bool   ->  0/1
        String -> "Hello world"; "123"; "\"" ...
    "Съставни" типове:
        Списъци / List
        Речници / Dict
        Редици / Tuple
        Множества / Set
    
"""




x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))
print(type(z))







# Присвояване на няколко променливи наведнъж
x,y,z = 3,5,7
print(y) # 5

x = y = z = 3



# размяна на стойността на две променливи
a = "a"
b = "b"

#начин 1:
c = a
a = b
b = c

#начин 2:
a,b = b,a





#  <======== Оператори за вход и изход ========>

x = input("Enter a number\n") #input operator
print(x)
 
x = input("enter anything")  # x=5
print(type(x))               # str

x = int(input("enter anything")) # x=12
print(type(x))                   # int




