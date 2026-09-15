# Проверка на код с `assert` и `pytest`

Тестът проверява дали функцията дава очаквания резултат. Пишете функциите така, че да **връщат** стойност; после ги проверявайте отделно.

```py
def is_even(number):
    return number % 2 == 0


assert is_even(4) is True
assert is_even(5) is False
assert is_even(0) is True
```

Ако условието на `assert` е невярно, Python спира с `AssertionError`.

## `pytest`

Инсталирайте го във виртуалната среда и създайте файл `test_main.py`:

```powershell
python -m pip install pytest
pytest
```

```py
from main import is_even


def test_even_number():
    assert is_even(4) is True


def test_odd_number():
    assert is_even(5) is False
```

За всяка функция проверете нормален случай, граничен случай (`0`, празен низ, празен списък) и невалиден вход, ако задачата го допуска.
