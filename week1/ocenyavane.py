
"""
Оценяване на студентите от специалност АД:

6 домашни работи - макс 10%
Примерен максимален резултат на всяка домашна работа:
1 - макс 1%
2 - макс 1%
3 - макс 2%
4 - макс 2%
5 - макс 2%
6 - макс 2%

3 контролни работи - макс 30%
1 - макс 10%
2 - макс 10%
3 - макс 10%

Участие в лекции и упражнения - макс 10%

Финален изпит - макс 50%

Скала за оценяване:
3 - 60%С
4 - 70%
5 - 80%
6 - 90%
"""


import sys


# функция за скалата за оценяване:

def scale(pr):
    if pr < 60:
        return 2
    elif pr < 70:
        return 3
    elif pr < 80:
        return 4
    elif pr < 90:
        return 5
    else:
        return 6



# Домашни работи:

hw_result = 0

for n in range(1, 7):
    result = float(input(f"Домашно {n}: "))
    if (n < 3 and (result > 1 or result < 0)) or (n >= 2 and (result > 2 or result < 0)):
        sys.exit("Този резултат не е възможен.")
    else:
        hw_result += result

print("Резултат от домашни:", hw_result)



# Контролни работи:

exam_result = 0
n = 1 # брой контролни работи

while n < 4:
    result = float(input(f"Контролна работа {n}: "))
    if result > 10 or result < 0:
        sys.exit("Този резултат не е възможен.")
    else:
        exam_result += result

    n += 1

print("Резултат от контролни:", exam_result)




# Активност по време на лекции и упражнения:

activity_result = float(input("Активност по време на лекции и упражнения: "))
if activity_result < 0 or activity_result > 10:
    sys.exit("Този резултат не е възможен.")


    
# Освобождаване от изпит:

result_without_fe = hw_result + exam_result + activity_result
print(result_without_fe)

if result_without_fe >= 35:
    final_result = result_without_fe * 2
    print(f"Вашият резултат за момента е: {result_without_fe} %.\nСлед умножението се получават {final_result} %, т.е. получавате оценка {scale(final_result)}.")
    yes_no = input("Доволни ли сте от оценката си?(yes/ no): ")
    if yes_no.lower() == "yes":
        sys.exit(f"Честито, завършихте успешно курса с оценка {scale(final_result)}")
    elif yes_no.lower() == "no":
        print("Тогава отивате на финален изпит.")
    else:
        sys.exit("Този резултат не е възможен.")
else:
    print("Отивате на финален изпит.")



# Финален изпит:

final_exam = float(input("Финален изпит: "))
if final_exam < 0 or final_exam > 50:
    sys.exit("Този резултат не е възможен.")



# Крайна оценка/ поправителен изпит:

final_result = result_without_fe + final_exam
print(f"Вашият резултат е: {final_result} %.\nПолучавате оценка {scale(final_result)}.")

if scale(final_result) == 2:
    print("Ще се видим на поправителната сесия!")



















    