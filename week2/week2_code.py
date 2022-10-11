# <============== Cast-ване на типове към други типове ==============> 
 
# от предния път
x = int(1)   # x ще е 1
y = int(2.8) # y ще е 2
z = int("3") # z ще е 3

# ново
x = float(1)     # x ще стане 1.0
y = float(2.8)   # y ще стане 2.8
z = float("3")   # z ще стане 3.0
w = float("4.2") # w ще стане 4.2

x = str("s1") # x ще стане 's1'
y = str(2)    # y ще стане '2'
z = str(3.0)  # z ще стане '3.0'














# <=========== String-ове ===========> 

"""
    Няма значение какви кавички ползваме в print() ф-ята.   Независимо дали " или ' резултатът е един и същ
"""
print("Hello")
print('Hello')


d = "Hello World"
print(d)
#print(D)   #<- case sensitive



# string на няколко реда
s = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(s)



x = "Hello "
y = "world!"
print(x + y) #    + конкатенира string-ове, като не добавя разстояние между тях
# съвет
x = "Hello"
y = "world!"
print(x + " " + y) # добавяйте си space-а на ръка в print ф-ята, защото иначе може много лесно да се объркате

# разбира се, не е нужно да пишем x + y в print() функцията, можем да си направим нова променлива която да е равна на x+y
x = "Hello"
y = "world!"
z = x + " " + y
print(z)




x = "Hello"
y = "World"
print(x,y) #    ,  конкатенира string-ове като добавя разстояние между тях


x = 5
y = "String"
#print(x + y)   няма да проработи, защото  +  опитва да събере числото със string-a
print(x , y)

y = "3"
# print(x + y)
#print(x + y) няма автоматично да смени типа на Y на int и да ги събере, тоест ще има грешка










# Представяне на string като редица от символи
"""
    Hello
    |H|e|l|l|o|
"""
s = "Hello"
# с квадратни скобки [] можем да достъпим избран символ от редицата от символи
# ВАЖНО - броенето винаги започва от 0, а НЕ от 1

print(s[0]) # H
print(s[1] + s[3]) # ?







# Дължина на дума
s = "Hello World!"
daljina = len(s)
print(daljina) # 12

# Проверка дали substring се съдържа в string
s = "Obicham da ucha vuv fmi!"
print("fmi" in s)   #  А какъв е типът на това което ще принтираме?

# Проверка дали substring не се съдържа в string
s = "Obicham da ucha vuv fmi!"
print("fmi" not in s)



# Одрязване на string
s = "Hello World!"
print(s[2:5])  # отново ползваме [] за да достъпим символи с номерация от 2 до 4 (включително, без символът на място 5) в s
print(s[:5])
print(s[2:])
print(s[-5:-2])  # Обратна индексация - "-5" означава 5тият символ отзад напред


# чрез обратната индексация можем да reverse-нем string
str = "Hello world!"
reversed = str[::-1]
print(reversed)


# използвайки стъпка можем да принтираме всеки n-ти символ от string
str = "Hello world!"
print(str[::2]) # принтира от началото до края на стринг-а, но само всеки втори символ






# Промени по един string
s = "Hello world!"
print(s.upper()) # HELLO WORLD!
print(s.lower()) # hello world!

s = "      Hello world!            "
print(s) # принтира се с табулациите отпред и отзад
print(s.strip()) # принтира без разстояния отпред и отзад на текста


# замяна на един символ с друг в string
s = "hello world"
print(s.replace('l', 'e'))


# split-ване на string
s = "Hello world!"
print(s.split(" "))  # ['Hello', 'world!']
print(s.split("l"))  # ['He', '', 'o wor', 'd!']





# добавяне на кавички в string 
s = "Liubimiqt mi serial e \"Alice in Borderland\"!"

"""
 \" -> "
 \' -> '
 \\ -> \
 \n -> нов ред
 \t -> табулация
 Има и други, но това са основните които ще ползвате
"""






# форматиране на string
name = "Vili"
age = 21
print(f"I am {name}, {age} years old.")        # f форматира текста, използвайки горните променливи и ги замества
print("I am" , name, ",", age, "years old.")   # е подобно на горното, но имайте впредвид екстра whitespace-а, който се добавя заради ","
 


# Бонус информация: 
# https://www.geeksforgeeks.org/python-string-methods/