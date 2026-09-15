# HTTP и API

API позволява на програмата да поиска данни или действие от друга услуга. Най-често получаваме JSON чрез HTTP заявка.

```powershell
python -m pip install requests
```

```py
import requests

url = "https://api.example.com/items"  # заменете с адреса от документацията на API-то

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.RequestException as error:
    print(f"Заявката не успя: {error}")
```

- `GET` взема данни; `POST` изпраща нови данни.
- `response.status_code` показва резултата: `200` е успех, `404` означава „не е намерено“, а `401` – липсва или е невалидно удостоверяване.
- `response.json()` преобразува JSON отговора в Python речник или списък.
- `timeout` предпазва програмата от безкрайно чакане.

Никога не записвайте API ключ в кода или GitHub. Пазете го в `.env`, добавете `.env` в `.gitignore` и четете стойността от environment variable.

## Допълнителни ресурси

- [Requests: quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
