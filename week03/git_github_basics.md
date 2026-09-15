# Git и GitHub: първи стъпки

**Git** пази история на промените в проект на вашия компютър. **GitHub** съхранява Git хранилището онлайн, за да го споделяте и архивирате.

## Настройване – прави се веднъж

```powershell
git config --global user.name "Вашето име"
git config --global user.email "your-email@example.com"
```

## Първи локален commit

Влезте в папката на проекта и изпълнете:

```powershell
git init
git status
git add main.py README.md
git commit -m "Add first program"
git log --oneline
```

`git status` показва какво е променено. `git add` избира какво ще влезе в следващия commit. `git commit` записва избраните промени с кратко, смислено съобщение.

## `.gitignore`

Създайте файл `.gitignore` още в началото:

```gitignore
.venv/
__pycache__/
.idea/
.env
```

Не качвайте пароли, API ключове или големи генерирани файлове.

## Публикуване в GitHub

1. Създайте празно repository в GitHub.
2. Копирайте неговия SSH или HTTPS адрес.
3. Свържете локалния проект и го качете:

```powershell
git remote add origin <адрес-на-repository>
git branch -M main
git push -u origin main
```

След това обновете страницата на repository-то в GitHub. Там трябва да виждате файловете и commit-а.

## Мини упражнение

Създайте папка с `main.py`, който извежда вашето име, и `README.md` с едно изречение за проекта. Направете commit и го качете в GitHub.

## Допълнителни ресурси

- [Git Book: започване с Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [GitHub Docs: Hello World](https://docs.github.com/en/get-started/using-github/hello-world)
