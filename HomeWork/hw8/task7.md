# PythonAnywhere з використанням бази даних SQLite.

**Мета:** Показати, що проєкт повністю працює на PythonAnywhere з SQLite та static.

## Кроки:

1. На PA: **git clone** → venv → **pip install -r requirements.txt**.
2. Перевір **settings.py**: DATABASES вказує на файл **db.sqlite3** у користувацькій папці.
3. **python manage.py migrate**
4. **python manage.py collectstatic**
5. У Web UI вкажи static mapping /static/ -> /home/youruser/yourproject/staticfiles.
6. Перезапусти Web app, перевір сторінки (головна, admin, ключові view).

---

## Обмеження SQLite на PA:
    - SQLite нормально працює для невеликих/демонстраційних проєктів.
    - Для багато-користувацької системи під навантаженням — використовуй Postgres (PA має опцію або окремий хост).

---