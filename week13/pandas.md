# Pandas
* модул на Python, който служи за анализ на данни от различни файлове

## 1. Серии
* наподобява едномерен масив (колона от таблица)
* има два начина на инициализация:
### I начин:
```py
import pandas as pd

a_list = ["Sofia", "Berlin", "Madrid"]

capital_cities = pd.Series(a_list)

print(capital_cities)
```
изход:
```
0     Sofia
1    Berlin
2    Madrid
dtype: object
```
#### имаме възможност да задаваме етикети вместо индекси:
```py
countries_capitals = pd.Series(a_list, index=["Bulgaria", "Germany", "Spain"])

print(countries_capitals)
```
изход:
```
Bulgaria     Sofia
Germany     Berlin
Spain       Madrid
dtype: object
```
### II начин:
```py
list1 = {"Bulgaria": "Sofia", "Germany": "Berlin", "Spain": "Madrid"}

countries_capitals = pd.Series(list1)

print(countries_capitals)
```
* селектиране на данни:
```py
print(pd.Series(list1, index=["Bulgaria", "Spain"]))
```
изход:
```
Bulgaria     Sofia
Spain       Madrid
dtype: object
```

## 2. DataFrames
* двумерна структура от данни, състояща се от серии (наподобява таблица с редове и колони)
```py
country_data = {
    "Bulgaria": ["Sofia", 680000],
    "Germany": ["Berlin", 83000000],
    "Spain": ["Madrid", 47800000]
}

df = pd.DataFrame(country_data)

print(df)
```
изход:
```
   Bulgaria   Germany     Spain
 0    Sofia    Berlin    Madrid
 1   680000  83000000  47800000
```
* задаване на етикети:
```py
df = pd.DataFrame(country_data, index=["capital", "population"])
print(df)
```
изход:
```
           Bulgaria   Germany     Spain
 capital      Sofia    Berlin    Madrid
 population  680000  83000000  47800000
```
* селектиране на данни:

### по колони:
```py
print(df["Bulgaria"])
```
изход:
```
 capital        Sofia
 population    680000
 Name: Bulgaria, dtype: object
```

### по редове: чрез `loc`

```py
print(df.loc["capital"])
```
изход:
```
 Bulgaria     Sofia
 Germany     Berlin
 Spain       Madrid
 Name: capital, dtype: object
```

## 3. Основни операции при работа с DataFrames

```py
import pandas as pd

uni_data = {
    "First Name": ["Ivan", "Petar", "Iordan", "Mirela", "Stela"],
    "Last Name": ["Ivanov", "Petrov", "Iordanov", "Slavova", "Kovacheva"],
    "Year of Study": [1, 1, 3, 2, 4],
    "Average Grade": [5.34, 4.5, 3.4, 5.51, 3.8]
}

df = pd.DataFrame(uni_data, index=["st1", "st2", "st3", "st4", "st5"])
```
###  a) добавяне на колона:
```py
df["Faculty Number"] = [12345, 67890, 23456, 78901, 34567]
```


### b) премахване на редове: 
* чрез `drop(labels)` - създава копие на df, където липсват посочените в labels индекси
```py
df_drop_row = df.drop("st1")
```
### c) премахване на колони: отново чрез `drop(labels)`
```py
df_drop_col = df.drop("Average Grade", axis="columns")
```
### d) разместване на редове/ създаване на нови редове без информация: 
* чрез `reindex(labels, fill_value - форматиране на NaN)`
```py
df_reindex = df.reindex(["st2", "st1", "st3", "st4", "st5", "st6"], fill_value="no info")
```

### e) oператори за анализиране на данни
```py
print(df.head(3)) # извежда първите 3 реда
print(df.tail(2)) # извежда последните 2 реда
print(df.info())
```
изход при `df.info()`:
```
<class 'pandas.core.frame.DataFrame'>
 Index: 5 entries, st1 to st5
 Data columns (total 5 columns):
     Column          Non-Null Count  Dtype
 ---  ------          --------------  -----
  0   First Name      5 non-null      object
  1   Last Name       5 non-null      object
  2   Year of Study   5 non-null      int64
  3   Average Grade   5 non-null      float64
  4   Faculty Number  5 non-null      int64
 dtypes: float64(1), int64(2), object(2)
 memory usage: 412.0+ bytes
 None
```

4. Cleaning Data

Ще разгледаме следната база от данни (можете да я откриете в мудъл и да си я изтеглите от там):
```py
import pandas as pd

df = pd.read_csv('big_cities_health_data_inventory.csv')

print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 13512 entries, 0 to 13511
# Data columns (total 11 columns):
#  #   Column                      Non-Null Count  Dtype
# ---  ------                      --------------  -----
#  0   indicator_category          13512 non-null  object
#  1   indicator                   13512 non-null  object
#  2   year                        13512 non-null  object
#  3   gender                      13512 non-null  object
#  4   race_ethnicity              13512 non-null  object
#  5   value                       13499 non-null  float64
#  6   place                       13512 non-null  object
#  7   bchc_requested_methodology  13004 non-null  object
#  8   source                      11222 non-null  object
#  9   methods                     4232 non-null   object
#  10  notes                       3541 non-null   object
# dtypes: float64(1), object(10)
# memory usage: 1.1+ MB
# None
```
* Извършваме Data Cleaning с цел премахване на излишните данни от нашата структура, за да може да заема по-малко памет в ОП. В следващите редове ще разгледаме основните проблеми, който могат да се срещнат в дадена база от данни, и тяхното решение.

### 1) празни клетки - могат да създадат проблем при анализирането на данните
- решение №1: `dropna(inplace = False)` - премахва редовете, съдържащи празни клетки
    --> `inplace = False` - създаване на нов DataFrame
    --> `inplace = True` - промяна на оригиналния DataFrame

- решение №2: `fillna(value, inplace = False)` - попълва на мястото на празните клетки value


### 2) грешен тип данни
- решение №1: премахване на редове чрез `dropna(subset=[...] - на избрано подмножество)`
- решение №2: конвертиране в правилния формат

### 3) нетипични данни за конкретната извадка
- решение №1: премахване на редове чрез `drop(row index)`
- решение №2: замяна с правилните чрез `loc[row index, column name]`

### 4) повтарящи се данни - използване на `drop_duplicates(inplace=False)`

#### добри примери можете да разгледате тук: https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
