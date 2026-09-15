# Работна среда: папки, терминал и пакети

Един проект е папка. В нея пазим кода, данните и кратък `README.md`, който обяснява какво прави проектът.

```text
my-project/
├── main.py
├── README.md
├── data/
└── .gitignore
```

## Терминалът в PyCharm

В PyCharm отворете **View → Tool Windows → Terminal**. Терминалът се отваря директно в папката на проекта, затова не е нужно да търсите папката ръчно. Полезни команди в PowerShell:

```powershell
Get-ChildItem       # показва файловете
cd име-на-папка     # влиза в папка
cd ..               # връща една папка назад
python main.py      # стартира програмата
```

## Виртуална среда и пакети

Виртуалната среда пази пакетите за конкретния проект, вместо да ги инсталира глобално.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests
python -m pip freeze > requirements.txt
```

Засега е достатъчно да знаете, че `.venv` е помощна папка на проекта. По-късно ще разгледаме как се работи с нея при споделяне на код и GitHub.

## Допълнителни ресурси

- [Терминалът в PyCharm](https://www.jetbrains.com/help/pycharm/terminal-emulator.html)
- [Официално ръководство за виртуални среди и пакети](https://docs.python.org/3/tutorial/venv.html)
