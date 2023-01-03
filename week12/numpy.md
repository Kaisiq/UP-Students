# Библиотеката NumPy
* библиотека, която се използва за ефективно извършване на математически и логически операции над масиви
* алтернативна програма - MatLab

## 1. Основни елементи
* нов тип данни - `ndarray` (многомерен компактен масив, съдържащ елементи от един и същи тип)
* задаване на размерност - `ndarray.ndim` (ndim = 3 -> тримерен масив)
* задаване на граници на тази размерност - `ndarray.shape` (shape = (2, 3) -> двумерен масив, като ndim = 2 == брой елементи в редицата на shape) с 2 реда и 3 стълба)
* брой елементи - `ndarray.size` (произведението от числава в shape)
* брой байтове, отделени за всеки елемент от масива - `ndarray.itemsize`
* тип данни в масива - ndarray.dtype

### Създаване на масив:
```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # едномерен масив // може да се запише и като np.arange(1,10)
print(arr)  # [1 2 3 4 5 6 7 8 9]
```

* `reshape(брой редове, брой колони, order)` - оразмерява масива
```py
reshaped_arr = arr.reshape((3, 3))  # двумерен масив с 3 реда и 3 колони (оразмеряване на масива)
print(reshaped_arr)  # [[1 2 3][4 5 6][7 8 9]]
```
## 2. Основни функции:

* `zeros(shape, dtype, order)` - задава масив от нули
```py
print(np.zeros((1, 2), "int"))  # array([[0, 0]])
```
* `ones(shape, dtype, order)` - задава масив от единици
```py
print(np.ones((1, 2), "int"))  # array([[1, 1]])
```
* `arange(start, stop, step)` - създава едномерен масив
```py
print(np.arange(2, 9, 4))  # array([2, 6])
```
* `linspace(min, max, (n) number of elements in array)` - създава едномерен масив от n елемента, съдържащ min и max, като стъпката я изчислява автоматично
```py
print(np.linspace(4, 10, 5, dtype="int"))  # array([ 4,  5,  7,  8, 10])
print(np.linspace(1, 2, 5, retstep=True))  # (array([1.  , 1.25, 1.5 , 1.75, 2.  ]), 0.25)
```
* `asarray` - конвертира в масив
```py
a_list = [[1, 2], [10, 20]]
print(type(np.asarray(a_list)))  # <class 'numpy.ndarray'>
```
## 3. Действия с масиви
### a) Умножение:
- поелементно:
```py
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)
# [1, 1], [0, 1]
#  *  *    *  *
# [2, 0], [3, 4]
#  =  =    =  =
# [2, 0], [0, 4]
```
- на матрици:
```py
print(A.dot(B))  # A = array([[5, 4],[3, 4]])
print(np.dot(A, B))  # C = array([[5, 4],[3, 4]])

print(A.sum())  # 1 + 1 + 0 + 1 = 3
print(A.min(initial=0))  # 0
print(A.max(initial=0))  # 1
print(B.sum(axis=0))  # array([5, 4]) -> сбор по колони (axis=1 - сбор по редове)
```
* забележка: `initial` е хубаво да бъде остойностявано, за да не даде грешка програмата, ако случайно масивът е празен.

### б) Достъп до елементите в масив:
```py
new_arr = np.arange(15, dtype="int").reshape((3, 5))
# [ 0,  1,  2,  3,  4]
# [ 5,  6,  7,  8,  9]
# [10, 11, 12, 13, 14]

arr1 = new_arr[0:2, 1:3]
print(arr1)
# [1, 2]
# [6, 7]

arr2 = new_arr[:, 1:]
print(arr2)
# [ 1,  2,  3,  4]
# [ 6,  7,  8,  9]
# [11, 12, 13, 14]

arr3 = new_arr[::2, ::3]  # през 1 ред / през 2 колони
print(arr3)
# [ 0,  3]
# [10, 13]
```
### в) Сортиране:
```py
num_array = np.array([12, -10, 5, 0, -223, 154])
num_array_sorted = np.sort(num_array)
print(num_array_sorted)

twodim_array = np.array([[12, -5, 3], [10, 32, -100]])
twodim_array_sorted = np.sort(twodim_array)  # сортиране по редове
print(twodim_array_sorted)

str_array = np.array(["java", "python", "c++"])
str_array_sorted = np.sort(str_array)
print(str_array_sorted)
```
* `searchsorted` - връща позицията (масив от числа) на число (числата в списък) в сортирания масив, ако евентуално е (са) част от масива:
```py
num_location_in_num_array = np.searchsorted(num_array_sorted, 10)
print(num_location_in_num_array)
num_location_in_num_array = np.searchsorted(num_array_sorted, [123, -40, 110])  # array([6, 2, 6], dtype=int64)
```
* `argsort` - връща масив от индексите на числата от масива след тяхното подреждане във възходящ ред
```py
import numpy as np

a = np.array([9, 3, 1, 7, 4, 3, 6])
print(a) # [9, 3, 1, 7, 4, 3, 6]

b = np.argsort(a)
print(b) # [2 1 5 4 6 3 0], т.е. а подреден изглежда по следния начин: [1 3 3 4 6 7 9]
```
* `lexsort(lastsort,firstsort)`

<img width="1055" alt="image" src="https://user-images.githubusercontent.com/114401128/210048785-f463a1b9-0b3e-4852-9ae2-ffef4346c7b7.png">

### реализация в Python:

```py
import numpy as np

a = np.array([9, 3, 1, 3, 4, 3, 6])
b = np.array([4, 6, 9, 2, 1, 8, 7])
print(np.lexsort((b, a))) # [2 3 1 5 4 6 0]
```

### г) Филтриране:
* `nonzero` - връща индексите на ненулевите елементи
* `where` - връща индексите на елементите, които отговарят на поставеното условие
```py
num_array = np.array([12, -10, 5, 0, -223, 154])
cond_array = np.where(num_array > 0)
print(cond_array)  # (array([0, 2], dtype=int64),)
```
* `extract` - извлича елементи, отговарящи на условие
```py
cond_num_array = np.extract(num_array > 0, num_array)
print(cond_num_array)  # array([12,  5])
```

### д) `copy` VS `view`
* `copy` е по-добро от view, ако искаме да не променяме първоначалния масив, който сме копирали
```py
a = np.array([1, 2, 3, 4, 5])
b = a.copy()
b[0] = 10
print(a[0], b[0])  # 1, 10
```
