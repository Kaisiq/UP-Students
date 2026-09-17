# Файлове: текст, CSV и JSON

Използвайте `with open(...)`, за да се затвори файлът автоматично, дори при грешка. Винаги указвайте `encoding="utf-8"` за текст на български.

## Текстов файл

```py
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Първи ред\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Режими: `"r"` чете, `"w"` презаписва или създава файл, а `"a"` добавя текст накрая.

## CSV

```py
import csv

with open("students.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["name"], row["grade"])
```

`DictReader` използва първия ред като имена на колони.

## JSON

```py
import json

student = {"name": "Ana", "grade": 5.5}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=2)

with open("student.json", encoding="utf-8") as file:
    loaded_student = json.load(file)
```

JSON е текстов формат за списъци, речници, числа, низове, `true`/`false` и `null`. При липсващ файл обработете `FileNotFoundError`.

## Следваща стъпка

[Продължете към Pandas и CSV данни](../week13/pandas.md)

## Допълнителни ресурси

- [Python Tutorial: вход и изход](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python документация за JSON](https://docs.python.org/3/library/json.html)
