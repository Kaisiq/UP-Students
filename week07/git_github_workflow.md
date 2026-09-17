# Git и GitHub: ежедневен работен процес

След като repository-то е публикувано, работете с кратък цикъл: **обнови → промени → провери → commit → push**.

```powershell
git pull
git status
git diff
git add .
git commit -m "Explain what changed"
git push
```

- `git pull` взема промените от GitHub. Правете го преди работа.
- `git diff` показва разликите преди commit-а.
- `git add .` добавя всички подходящи промени; при съмнение добавяйте конкретни файлове вместо това.
- `git push` качва новите commits.

Полезно е и клонирането на вече съществуващ проект:

```powershell
git clone <адрес-на-repository>
cd <име-на-папка>
```

Използвайте кратки commits с една цел: `Add input validation`, `Fix CSV parsing`. Не правете commit на `.env`, `.venv/` или пароли.

## Следваща стъпка

[Продължете към `map`, `filter` и `reduce`](../week08/methods.md)

## Допълнителни ресурси

- [Git Book: работа с remote repositories](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [GitHub Docs: игнориране на файлове](https://docs.github.com/en/get-started/git-basics/ignoring-files)
